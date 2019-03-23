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
import subprocess
import json
import os
import time

def index(request):
	return render(request, 'index.html')

def request_page(request):
	return render(request, 'query/query.html', {})

def make_query(request):
	
	keyword = request.POST.get("keyword")
	count = request.POST.get("count")
	
	str1 = "massmine --task=twitter-search --count="
	str2 = " --query="
	str3 = " | jsan --output="
	str4 = ".csv"

	command = str1 + count + str2 + "\""+keyword+"\"" + str3 + keyword + str4


	print(os.popen('pwd').read())
	df = pd.read_csv('/home/josh/Documents/SeniorProject/Massmine-for-the-Masses/src/webapp/'+keyword+'.csv')

	new_study = Study(user="MEEEE",study_id=keyword+str(int(time.time())))
	new_study.save()

	for row in df.iterrows():
	    for x in range(1,len(row)):
	        id_str = row[x]['id_str']
	        tweet_text = row[x]['text']
	        new_study.tweets.create(tweet_id_str = id_str,text = tweet_text)
	new_study.save()

	return HttpResponse("Success!")

	# massmine --task=twitter-stream --query=love --count=200 | jsan --output=mydata.csv
