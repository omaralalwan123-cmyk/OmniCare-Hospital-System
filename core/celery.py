import os
import django
from celery import Celery
from celery.schedules import crontab

# 1. إعداد متغيرات نظام دجانجو الأساسية
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# 2. تعريف كائن سيلري لمشروع OmniCare
app = Celery('OmniCare')

# قراءة الإعدادات من ملف settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# 3. إعداد جدول المهام الدورية (Beat Schedule)
app.conf.beat_schedule = {
    'run-daily-appointments-morning': {
        'task': 'apps.medical_core.notifications.tasks.appointments.send_daily_morning_reminders',
        'schedule': crontab(minute=0, hour=7),
        'args': ('shifa',), 
    },
    'run-hourly-upcoming-appointments': {
        'task': 'apps.medical_core.notifications.tasks.appointments.send_hourly_upcoming_reminders',
        'schedule': 3600.0,
        'args': ('shifa',),
    },
}

# 4. إصلاح خطأ الـ Registry: تهيئة دجانجو أولاً ثم البحث عن المهام
django.setup()

app.autodiscover_tasks()

app.autodiscover_tasks(
    packages=['apps.medical_core.notifications'],
    related_name='tasks.appointments',
    force=True
)