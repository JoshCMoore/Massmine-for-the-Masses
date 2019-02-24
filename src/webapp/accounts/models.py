# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    oauth = models.CharField(max_length=50, blank=True)

    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username
