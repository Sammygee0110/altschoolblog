from django.forms import ModelForm
from .models import Blog
from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body"]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')