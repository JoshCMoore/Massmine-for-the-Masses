# query/forms.py

from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
		fields = ('oauth', 'bio')

class QueryForm(forms.Form):
	keyword = forms.CharField(max_length = 50)
	count = forms.IntegerField(max_length = 10)
