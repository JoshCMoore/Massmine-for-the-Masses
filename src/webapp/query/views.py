# query/views.py

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import reverse
import datetime
import subprocess
import json
import os

def index(request):
	return render(request, 'index.html')

def request_page(request):
	return render(request, 'query/query.html', {})

def make_query(request):
	
	keyword = request.POST.get('keyword')
	count = request.POST.get('count')
	
	#process = subprocess.Popen(['touch test.txt'])

	os.system('massmine --task=twitter-search --count=200 --query=love --output=mydata.json')

	return HttpResponse("success")

	# massmine --task=twitter-search --count=200 --query=love --output=mydata.json