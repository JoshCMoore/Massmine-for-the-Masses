#Defining the celery module used for asynchronous tasks

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webappproject.settings')

app = Celery('webapp')

#Gives celery config keys the CELERY prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

#Load all task modules
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

