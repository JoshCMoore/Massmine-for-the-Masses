# query/views.py

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import reverse
from query.models import Tweet
from analysis.models import Study
import pandas as pd
#import numpy as np
import datetime
from subprocess import Popen, PIPE
import json
import os
import time

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
	
	keyword = request.POST.get("keyword")
	count = request.POST.get("count")
	
	str1 = "massmine --task=twitter-search --count="
	str2 = " --query="
	str3 = " | jsan --output="
	str4 = ".csv"

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

	return HttpResponse("Success!")

	# massmine --task=twitter-stream --query=love --count=200 | jsan --output=mydata.csv
# 	#process = subprocess.Popen(['touch test.txt'])
# 	command = 'massmine --task=twitter-search --count=' + count + ' --query=' + keyword 
# 	#os.system('massmine --task=twitter-search --count=200 --query=love --output=mydata.json')
# 	stdout = Popen(command, shell=True, stdout=PIPE).stdout 
# 	output = stdout.read()
# 	return HttpResponse(output)
# 
#  	# massmine --task=twitter-search --count=200 --query=love --output=mydata.json
