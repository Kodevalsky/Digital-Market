from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('about')
        form = LoginForm()
        context = {'form': form}
        return render(request, "login/login_view.html", context)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('about')
        messages.error(request, f'Invalid username or password')
        context = {'form': form}
        return render(request, "login/login_view.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, f"You have been logged out.")
    return redirect('login')
