# analysis/urls.py

from django.conf.urls import url
from analysis import views

# SET THE NAMESPACE!
app_name = 'analysis'

urlpatterns=[
    url(r'^analysis/$',views.analysis,name='analysis'),
    url(r'^create_analysis/$',views.create_analysis,name='create_analysis'),
    url(r'^graph/$', views.graph, name = 'graph'),
]

