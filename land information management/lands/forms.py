from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))




class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Please ,enter your name.')

    email = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
    address = forms.CharField(max_length=150, required=True, help_text='Required')
    city = forms.CharField(max_length=150, required=True, help_text='Required.')
    state = forms.CharField(max_length=150, required=False, help_text='Optional.')
    country = forms.CharField(max_length=150, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2','address','city','state','country' )