from django.shortcuts import render
from accounts.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import subprocess
import json

def test(request):
	search = request.POST.get('Search_Term')
	number = request.POST.get('Number_Of_Tweets')
	args = ["-t twitter-search","-c",number,"-q","\""+search+"\""]
	command = "massmine"
	for a in args:
		command+=" "+a
	process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
	output, error = process.communicate()

	return HttpResponse(output)

def request(request):
	return render(request, 'massminetest/index.html')

# Create your views here.
