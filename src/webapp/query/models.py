# query/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile

class Tweet(models.Model):
	
	# from tweet object api
	#created_at = models.DateTimeField(blank=False)
	tweet_id_str = models.CharField(max_length=100,default="") # string of tweet ID
	text = models.TextField(max_length=280,default="") # text of tweet
	# country = models.CharField(max_length=200,blank=True) #within place[]
	# device = models.CharField(max_length=100, blank=True)
	# truncated = models.BooleanField(null=True)
	# in_reply_to_status_id_str = models.CharField(max_length=100, null=True)
	# in_reply_to_user_id_str = models.CharField(max_length=100, null=True)
	# in_reply_to_screen_name = models.CharField(max_length=100, null=True)
	# retweet_count = models.IntegerField(default=0)
	# lang = models.CharField(max_length=100,blank=True, null=False)
	# 
	# # from user object api
	# user_id_str = models.CharField(max_length=100, unique=True, blank=False) # string of user id
	# name = models.CharField(max_length=100, blank=False,null=True) # user real name
	# screen_name = models.CharField(max_length=100, blank=False,null=True) # screen name
	# location = models.CharField(max_length=100, null=True) # string of user city/state etc
	# url = models.CharField(max_length=100, null=True) # url of twitter profile
	# description = models.CharField(max_length=300, null=True) # twitter profile - user description
	# verified = models.BooleanField(null=False)
	# followers_count = models.IntegerField(default=0)
	# friends_count = models.IntegerField(default=0)
	# listed_count = models.IntegerField(default=0) # num lists user is member of
	# favourites_count = models.IntegerField(default=0) # num user's tweets favorited by others
	# num_tweets = models.IntegerField(default=0) # num tweeets issued by user(incl retweets)
	# user_created_at = models.DateTimeField(blank=False)
	# utc_offset = models.IntegerField(null=True)
	# #time_zone = TimeZoneField(null=True)
	# geo_enabled = models.BooleanField(null=True)
