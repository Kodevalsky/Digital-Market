from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, UserChangeForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.

class LoginView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('about')
        form = LoginForm()
        context = {'form': form}
        return render(request, "login/login_view.html", context)
    def post(self, request):
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

def LogoutView(request):
    logout(request)
    messages.success(request, f"You have been logged.")
    return redirect('login')

class SignupView(TemplateView):
    def get(self, request):
        form = RegisterForm()
        context = {'form':form}
        return render(request, 'login/signup_view.html', context)
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('browse')
        messages.error(request, f'Signup failed, invalid data')
        context = {'form':form}
        return render(request, 'login/signup_view.html', context)
    
class ProfileView(TemplateView):
    def post(self, request):
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
            form = UserChangeForm(instance=request.user)
        return redirect('user_profile')

    def get(self, request):
        UsersDatabase = User.objects.all()
        TargetUser = UsersDatabase.get(username=request.user.username)
        context = {'user': TargetUser, 'user_form' : UserChangeForm()}
        return render(request, 'login/user_profile.html', context)

