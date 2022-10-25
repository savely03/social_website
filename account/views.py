from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash


# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', context={'section': 'dashboard'})


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', context={'new_user': new_user})
    return render(request, 'account/register.html', context={'form': form})


@login_required
def edit(request):
    user_form = UserEditForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    return render(request, 'account/edit.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'section': 'edit_profile'})


class CustomPasswordChangeView(PasswordChangeView):
    def get_context_data(self, **kwargs):
        context = super(CustomPasswordChangeView, self).get_context_data(**kwargs)
        context['section'] = 'password_change'
        return context
