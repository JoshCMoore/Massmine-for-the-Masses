from __future__ import absolute_import, unicode_literals

#makes sure Celery is always imported, important for shared_task decorator
from .celery import app as celery_app

__all__ = ('celery_app',)
