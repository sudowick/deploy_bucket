from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('gallery-home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/index.html', {'form': form})
    
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {'form':form})
