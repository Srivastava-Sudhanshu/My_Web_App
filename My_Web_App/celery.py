from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from pytz import timezone
from .settings import BASE_REDIS_URL
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Web_App.settings')


app = Celery('My_Web_App')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


app.conf.beat_schedule = {
    'send-mail-every-minute-contrab': {
        'task': 'Accounts.tasks.DueFeeNotification',
        'schedule': crontab(hour=14,minute=45),
    },
}

