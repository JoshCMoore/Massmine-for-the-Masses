# query/views.py

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import reverse
from query.forms import QueryForm
from query.models import Tweet
from analysis.models import Study
from accounts.models import Profile
from subprocess import Popen, PIPE
from django.contrib.auth.decorators import login_required
import pexpect
import subprocess
import os
import json
import time

def index(request):
	return render(request, 'index.html')

def request_page(request):
	return render(request, 'query/query.html', {})

def validate_massmine(request):

	my_profile = instance=request.user.profile
	consumer_key = my_profile.consumer_key
	consumer_secret = my_profile.consumer_secret
	access_token = my_profile.access_token
	access_token_secret = my_profile.access_token_secret

	child = pexpect.spawn('massmine --task=twitter-auth')
	child.expect('[No]')
	child.sendline('yes')
	child.expect('Consumer key:')
	child.sendline(consumer_key)
	child.expect('Consumer secret:')
	child.sendline(consumer_secret)
	child.expect('Access token')
	child.sendline(access_token)
	child.expect('Access token secret')
	child.sendline(access_token_secret)
	child.wait()
	#exit status should be 0 on a success, 1 on a fail. signal status is if something else interrupted the command.
	return(child.exitstatus)

@login_required
def make_query(request):

	if (validate_massmine(request) == 1):
		return render(request, 'query/query_error.html', {})
	else:
		keyword = request.POST.get('keyword')
		count = request.POST.get('count')

		command = 'massmine --task=twitter-search --count=' + count + ' --query=' + '"'+keyword+'"'

		stdout = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

		output = stdout.readlines()

		hshtg = None
		keyword = keyword.replace(' ','_')
		new_study = Study(user=str(request.user),study_id=keyword+str(int(time.time())))
		new_study.save()

		for i in output:
			string = i.decode("utf-8")
			data = json.loads(string)

			try:

				for key,value in data.items():
					if (key == 'id_str'):
						tid = value
					if (key == 'created_at'):
						ca = value
					if (key == 'text'):
						txt = value
					if (key == 'source'):
						src = value
					if (key == 'truncated'):
						trunc = value
					if (key == 'retweet_count'):
						re_count = value
					if (key == 'metadata'):
						for key,value in data['metadata'].items():
							if (key == 'iso_language_code'):
								language = value
					if (key == 'entities'):
						for key,value in data['entities'].items():
							if (key == 'hashtags'):
								for n in data['entities']['hashtags']:
									hshtg  = n['text']
					if (key == 'user'):
						for key,value in data['user'].items():
							if (key == 'id_str'):
								uid = value
							if (key == 'location'):
								cntry = value
							if (key == 'name'):
								nme = value
							if (key == 'screen_name'):
								scr_name= value
							if (key == 'url'):
								u = value
							if (key == 'description'):
								desc = value
							if (key == 'verified'):
								verify = value
							if (key == 'followers_count'):
								fol_count = value
							if (key == 'listed_count'):
								list_count = value
							if (key == 'favourites_count'):
								fav_count = value
							if (key == 'statuses_count'):
								tw_count = value
							if (key == 'utc_offset'):
								utc_off = value
							if (key == 'friends_count'):
								fr_count = value
							if (key == 'time_zone'):
								tz = value
							if (key == 'geo_enabled'):
								geo_en = value
					if (key == 'in_reply_to_status_id_str'):
						reply_sid = value
					if (key == 'in_reply_to_user_id_str'):
						reply_uid = value
					if (key == 'in_reply_to_screen_name'):
						reply_scrname = value

				new_study.tweets.create(tweet_id_str=tid,created_at=ca,text=txt,device=src,truncated=trunc,
						retweet_count=re_count,lang=language,country=cntry,user_id_str=uid,name=nme,
						screen_name=scr_name,in_reply_to_status_id_str=reply_sid,in_reply_to_user_id_str=reply_uid,
						in_reply_to_screen_name=reply_scrname,hashtags=hshtg,url=u,
						description=desc,verified=verify,followers_count = fol_count,friends_count=fr_count,
						listed_count=list_count,favourites_count=fav_count,num_tweets=tw_count,
						utc_offset=utc_off,time_zone=tz,geo_enabled=geo_en)

			except Exception as e:
				print(e)
			
		return render(request, 'query/query_complete.html', {})