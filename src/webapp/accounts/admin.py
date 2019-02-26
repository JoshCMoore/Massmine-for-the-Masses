# accounts/admin.py

from django.contrib import admin
from accounts.models import UserProfile,User



admin.site.register(UserProfile)
