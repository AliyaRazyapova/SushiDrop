import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sushidrop.settings')

app = Celery('sushidrop', broker='redis://localhost:6379/0')
app.autodiscover_tasks()

from core.tasks import send_discount_emails