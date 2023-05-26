from celery import Celery

app = Celery('sushidrop', broker='redis://localhost:6379/0')
app.autodiscover_tasks()
