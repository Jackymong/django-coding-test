from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import User

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input','placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input','placeholder':'Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']