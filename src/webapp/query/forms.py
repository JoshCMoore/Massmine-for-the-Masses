# query/forms.py

from django import forms
from accounts.models import Profile
from query.models import Tweet

class QueryForm(forms.ModelForm):
	keyword = forms.CharField(max_length = 50)
	count = forms.IntegerField(max_length = 10)

	class Meta:
		model = Tweet
		#fields = '__all__'
		# test- store only one field
		fields = ('tweet_id_str',)