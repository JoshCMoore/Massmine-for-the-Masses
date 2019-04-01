# query/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile
from datetime import datetime

class Tweet(models.Model):
	
	# from tweet object api
<<<<<<< HEAD
	#created_at = models.DateTimeField(blank=False)
	tweet_id_str = models.CharField(max_length=100,default="") # string of tweet ID
	text = models.TextField(max_length=280,default="") # text of tweet
	country = models.CharField(max_length=200,blank=True,default="") #within place[]
	device = models.CharField(max_length=100, blank=True,default="")
	# truncated = models.BooleanField(null=True)
	# in_reply_to_status_id_str = models.CharField(max_length=100, null=True)
	# in_reply_to_user_id_str = models.CharField(max_length=100, null=True)
	# in_reply_to_screen_name = models.CharField(max_length=100, null=True)
	retweet_count = models.IntegerField(default=0)
	lang = models.CharField(max_length=100,default="")
	# from user object api
	# user_id_str = models.CharField(max_length=100, unique=True, blank=False) # string of user id
	# name = models.CharField(max_length=100, blank=False,null=True) # user real name
	screen_name = models.CharField(max_length=100, default="")  # screen name
	# location = models.CharField(max_length=100, null=True) # string of user city/state etc
	# url = models.CharField(max_length=100, null=True) # url of twitter profile
	# description = models.CharField(max_length=300, null=True) # twitter profile - user description
	# verified = models.BooleanField(null=False)
	followers_count = models.IntegerField(default=0)
	# friends_count = models.IntegerField(default=0)
	# listed_count = models.IntegerField(default=0) # num lists user is member of
	# favourites_count = models.IntegerField(default=0) # num user's tweets favorited by others
	# num_tweets = models.IntegerField(default=0) # num tweeets issued by user(incl retweets)
	# user_created_at = models.DateTimeField(blank=False)
	# utc_offset = models.IntegerField(null=True)
	# #time_zone = TimeZoneField(null=True)
	# geo_enabled = models.BooleanField(null=True)
=======
	tweet_id_str = models.CharField(max_length=100, default='tweet_id_str', primary_key=True) # string of tweet ID
	created_at = models.CharField(max_length=100, default='created_at', null=False)
	text = models.TextField(max_length=280, default='TextField') # text of tweet
	device = models.CharField(max_length=100, default='device') # listed as source in tweet data
	truncated = models.BooleanField(default=False)
	retweet_count = models.IntegerField(default=0)
	lang = models.CharField(max_length=100, default='language')
	country = models.CharField(max_length=200, default="usa") #within place[]
	in_reply_to_status_id_str = models.CharField(max_length=100, default='in_reply_to_status_id_str', null=True)
	in_reply_to_user_id_str = models.CharField(max_length=100, default='in_reply_to_user_id_str', null=True)
	in_reply_to_screen_name = models.CharField(max_length=100, default='in_reply_to_screen_name', null=True)
	
	#from user object api
	user_id_str = models.CharField(max_length=100, default='user_id_str') # id_str within 
	name = models.CharField(max_length=100, default='name') # user real name
	screen_name = models.CharField(max_length=100, default='screen_name') # screen name
	url = models.CharField(max_length=100, default='urls', null=True) # url of twitter profile
	description = models.CharField(max_length=300, default='description') # twitter profile - user description
	verified = models.BooleanField(default=False)
	followers_count = models.IntegerField(default=0)
	friends_count = models.IntegerField(default=0)
	listed_count = models.IntegerField(default=0) # num lists user is member of
	favourites_count = models.IntegerField(default=0) # num user's tweets favorited by others
	num_tweets = models.IntegerField(default=0) # num tweeets issued by user(incl retweets)
	user_created_at = models.DateTimeField(null=True)
	utc_offset = models.CharField(max_length=100, default='utc_offset', null=True)
	time_zone = models.DateTimeField(null=True)
	geo_enabled = models.BooleanField(default=False)
>>>>>>> logan
