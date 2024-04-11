from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        #this specifies the fields that should show up and in what order
        fields = ['username', 'email', 'password1','password2']