# query/forms.py

from django import forms
from query.models import Tweet

class QueryForm(forms.ModelForm):
	keyword = forms.CharField()
	count = forms.IntegerField()

	class Meta:
		model = Tweet
		fields = '__all__'
		#fields = ('tweet_id_str', 'created_at', 'text', 'device',)
