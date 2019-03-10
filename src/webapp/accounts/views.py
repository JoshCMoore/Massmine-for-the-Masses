# accounts/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserRegistrationForm, ProfileForm, EditUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db import transaction

def index(request):
    return render(request,'index.html')

def login_error(request):
    return render(request,'login_error.html')

def account_inactive_error(request):
    return render(request,'account_inactive_error.html')

@login_required
def password_change_error(request):
    return render(request,'password_change_error.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.oauth = form.cleaned_data.get('oauth')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            return render(request, 'index.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', 
            {'form':form})

@login_required
@transaction.atomic
def edit_user_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('index'))
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_user_profile.html', 
            {'user_form':user_form, 'profile_form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('index'))
        else:
            return render(request,'accounts/password_change_error.html', {})
	    #form not valid
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'accounts/change_password.html', args)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'accounts/account_inactive_error.html',{})
        else:
            return render(request,'accounts/login_error.html', {}) 
	    #username or password incorrect
    else:
        return render(request, 'accounts/login.html', {})
