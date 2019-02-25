
# analysis/views.py

from django.shortcuts import render
<<<<<<< HEAD
=======
from accounts.forms import UserForm,UserProfileInfoForm
>>>>>>> origin/development
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def analysis(request):
    return render(request, 'analysis/analysis.html', {})

def create_analysis(request):
	if request.method == 'POST':
		return HttpResponse("This is where I'll show analyses")
	else:
		return HttpResponse("I'll add error handling here.")
