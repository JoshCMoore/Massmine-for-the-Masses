# massminetest/urls.py

from django.conf.urls import url
from massminetest import views

# SET THE NAMESPACE!
app_name = 'massminetest'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^test/$',views.test,name='test'),
	url(r'^request/$',views.request,name='massminerequest'),

]
