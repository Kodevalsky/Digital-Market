from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class':"tw-px-3 tw-block tw-w-full tw-rounded-md tw-border tw-border-gray-800  tw-py-1.5 tw-text-gray-900 tw-shadow-sm tw-ring-1 tw-ring-inset tw-ring-gray-300 placeholder:tw-text-gray-400 sm:tw-text-sm sm:tw-leading-6"}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class':"tw-px-3 tw-block tw-w-full tw-rounded-md tw-border tw-border-gray-800 tw-py-1.5 tw-text-gray-900 tw-shadow-sm tw-ring-1 tw-ring-inset tw-ring-gray-300 placeholder:tw-text-gray-400 sm:tw-text-sm sm:tw-leading-6"}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "username", "password2")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"tw-block tw-w-full tw-px-5 tw-py-3 tw-mt-2 tw-text-gray-700 tw-placeholder-gray-400 tw-bg-white tw-border tw-border-gray-200 tw-rounded-md dark:tw-placeholder-gray-600 dark:tw-bg-gray-900 dark:tw-text-gray-300 dark:tw-border-gray-700 focus:tw-border-blue-400 dark:focus:tw-border-blue-400 focus:tw-ring-blue-400 focus:tw-outline-none focus:tw-ring focus:tw-ring-opacity-40"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"tw-block tw-w-full tw-px-5 tw-py-3 tw-mt-2 tw-text-gray-700 tw-placeholder-gray-400 tw-bg-white tw-border tw-border-gray-200 tw-rounded-md dark:tw-placeholder-gray-600 dark:tw-bg-gray-900 dark:tw-text-gray-300 dark:tw-border-gray-700 focus:tw-border-blue-400 dark:focus:tw-border-blue-400 focus:tw-ring-blue-400 focus:tw-outline-none focus:tw-ring focus:tw-ring-opacity-40"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"tw-block tw-w-full tw-px-5 tw-py-3 tw-mt-2 tw-text-gray-700 tw-placeholder-gray-400 tw-bg-white tw-border tw-border-gray-200 tw-rounded-md dark:tw-placeholder-gray-600 dark:tw-bg-gray-900 dark:tw-text-gray-300 dark:tw-border-gray-700 focus:tw-border-blue-400 dark:focus:tw-border-blue-400 focus:tw-ring-blue-400 focus:tw-outline-none focus:tw-ring focus:tw-ring-opacity-40"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"tw-block tw-w-full tw-px-5 tw-py-3 tw-mt-2 tw-text-gray-700 tw-placeholder-gray-400 tw-bg-white tw-border tw-border-gray-200 tw-rounded-md dark:tw-placeholder-gray-600 dark:tw-bg-gray-900 dark:tw-text-gray-300 dark:tw-border-gray-700 focus:tw-border-blue-400 dark:focus:tw-border-blue-400 focus:tw-ring-blue-400 focus:tw-outline-none focus:tw-ring focus:tw-ring-opacity-40"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"tw-block tw-w-full tw-px-5 tw-py-3 tw-mt-2 tw-text-gray-700 tw-placeholder-gray-400 tw-bg-white tw-border tw-border-gray-200 tw-rounded-md dark:tw-placeholder-gray-600 dark:tw-bg-gray-900 dark:tw-text-gray-300 dark:tw-border-gray-700 focus:tw-border-blue-400 dark:focus:tw-border-blue-400 focus:tw-ring-blue-400 focus:tw-outline-none focus:tw-ring focus:tw-ring-opacity-40"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"tw-block tw-w-full tw-px-5 tw-py-3 tw-mt-2 tw-text-gray-700 tw-placeholder-gray-400 tw-bg-white tw-border tw-border-gray-200 tw-rounded-md dark:tw-placeholder-gray-600 dark:tw-bg-gray-900 dark:tw-text-gray-300 dark:tw-border-gray-700 focus:tw-border-blue-400 dark:focus:tw-border-blue-400 focus:tw-ring-blue-400 focus:tw-outline-none focus:tw-ring focus:tw-ring-opacity-40"}))

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")
    