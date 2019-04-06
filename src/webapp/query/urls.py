# query/urls.py

from django.conf.urls import url
from query import views

# SET THE NAMESPACE!
app_name = 'query'

# Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    url(r'^request_page/$', views.request_page, name='request_page'),
    url(r'^make_query/$', views.make_query, name='make_query'),
]
