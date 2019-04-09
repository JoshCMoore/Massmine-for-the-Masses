from django.db import models
from query.models import Tweet

class Study(models.Model):
	user = models.CharField('user',max_length=60)
	study_id = models.CharField('study_id',max_length=100)
	tweets = models.ManyToManyField(Tweet)
