# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret')

class UserRegistrationForm(UserCreationForm):
    consumer_key = forms.CharField(max_length = 50, required = True)
    consumer_secret = forms.CharField(max_length = 50, required = True)
    access_token = forms.CharField(max_length = 50, required = True)
    access_token_secret = forms.CharField(max_length = 50, required = True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name')


