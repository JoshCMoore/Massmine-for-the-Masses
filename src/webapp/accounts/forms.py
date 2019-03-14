# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('oauth', 'bio')

class UserRegistrationForm(UserCreationForm):
    oauth = forms.CharField(max_length = 50, help_text='Required. This is your Twitter key used to access the api.')
    bio = forms.CharField(max_length = 500, required=False)

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name')
