# query/views.py

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import reverse
from query.models import Tweet
import pandas as pd
import numpy as np
import datetime
import subprocess
import json
import os

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

	command = str1 + count + str2 + "\""+keyword+"\"" + str3 + "\""+keyword+"\"" + str4

	os.system(command)

	df = pd.read_csv('/home/parallels/django/webapp/'+keyword+'.csv')

	for row in df.iterrows():
	    for x in range(1,len(row)):
	    	#need code here to insert into DB
	        #created_at = row[x]['created_at']
	        tweet_id_str = row[x]['id_str']
	        #print(tweet_id_str)
	        text = row[x]['text']
	        tweet_instance = Tweet.objects.create()
	        tweet_instance.save(tweet_id_str)

	return HttpResponse("Success!")

	# massmine --task=twitter-stream --query=love --count=200 | jsan --output=mydata.csv
