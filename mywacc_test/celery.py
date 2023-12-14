
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywacc_test.settings')

app = Celery('mywacc_test')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from all installed apps
app.autodiscover_tasks()
