# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    oauth = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return u"%s" % self.user

#    def __str__(self):
#        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = user.userprofile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=UserProfile)
