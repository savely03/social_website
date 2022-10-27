from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.contrib import messages


@login_required
def image_create(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image successfully added')
            return redirect(new_item.get_absolute_url)
    return render(request, 'image/create.html', context={'form': form, 'section': 'images'})
