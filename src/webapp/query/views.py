# query/views.py

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import reverse
from query.forms import QueryForm
from query.models import Tweet
<<<<<<< HEAD
from analysis.models import Study
=======
from subprocess import Popen, PIPE
>>>>>>> logan
import pandas as pd
#import numpy as np
import datetime
from subprocess import Popen, PIPE
import json
<<<<<<< HEAD
import os
import time
=======
import ast
>>>>>>> logan

def index(request):
	return render(request, 'index.html')

def request_page(request):
	return render(request, 'query/query.html', {})

def get_studies(request):
	context ={'studies_html':""} 
	for x in Study.objects.all():
		context['studies_html']+=("<li>"+x.study_id[:-10]+"</li>")
	return render(request, 'query/get_studies.html', context)

def make_query(request):
	
	keyword = request.POST.get('keyword')
	count = request.POST.get('count')

	command = 'massmine --task=twitter-search --count=' + count + ' --query=' + keyword

	stdout = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

	output = stdout.readlines()

	for i in output:
		string = i.decode("utf-8")
		data = json.loads(string)

<<<<<<< HEAD
	command = str1 + count + str2 + "\""+keyword+"\"" + str3 + keyword + str4

	os.system(command)
	
	df = pd.read_csv('/home/josh/Documents/SeniorProject/Massmine-for-the-Masses/src/webapp/'+keyword+'.csv')
	new_study = Study(user=str(request.user),study_id=keyword+str(int(time.time())))
	new_study.save()

	for row in df.iterrows():
		for x in range(1,len(row)):
			id_str = row[x]['id_str']
			tweet_text = row[x]['text']
			tweet_country = row[x]['place:country_code']
			tweet_device = row[x]['source']
			tweet_retweet_count = row[x]['retweet_count']
			tweet_lang = row[x]['lang']
			tweet_user = row[x]['user:screen_name']
			tweet_followers_count = row[x]['user:followers_count']
			new_study.tweets.create(tweet_id_str = id_str,text = tweet_text, country = tweet_country, device = tweet_device, retweet_count = tweet_retweet_count, lang = tweet_lang, screen_name = tweet_user, followers_count = tweet_followers_count)
=======
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

			tweet = Tweet(tweet_id_str=tid,created_at=ca,text=txt,device=src,truncated=trunc,
				retweet_count=re_count,lang=language,country=cntry,user_id_str=uid,name=nme,
				screen_name=scr_name,in_reply_to_status_id_str=reply_sid,
				in_reply_to_user_id_str=reply_uid,in_reply_to_screen_name=reply_scrname,url=u,description=desc,verified=verify,
				followers_count = fol_count,friends_count=fr_count,listed_count=list_count,favourites_count=fav_count,
				num_tweets=tw_count,utc_offset=utc_off,time_zone=tz,geo_enabled=geo_en)

			tweet.save()
>>>>>>> logan

		except:
			print("ERROR")
		
	return HttpResponse(output)

<<<<<<< HEAD
	# massmine --task=twitter-stream --query=love --count=200 | jsan --output=mydata.csv
# 	#process = subprocess.Popen(['touch test.txt'])
# 	command = 'massmine --task=twitter-search --count=' + count + ' --query=' + keyword 
# 	#os.system('massmine --task=twitter-search --count=200 --query=love --output=mydata.json')
# 	stdout = Popen(command, shell=True, stdout=PIPE).stdout 
# 	output = stdout.read()
# 	return HttpResponse(output)
# 
#  	# massmine --task=twitter-search --count=200 --query=love --output=mydata.json
=======
>>>>>>> logan
