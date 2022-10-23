from django.shortcuts import render, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', context={'section': 'dashboard'})
