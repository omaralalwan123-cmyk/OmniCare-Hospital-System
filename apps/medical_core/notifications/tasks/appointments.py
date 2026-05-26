from celery import shared_task
from django_tenants.utils import schema_context
from apps.medical_core.notifications.utils import send_global_notification
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_daily_morning_reminders(tenant_schema_name):
    current_date = timezone.now().date()
    logger.info(f"🌅 [Crontab] Starting daily morning appointment check for date {current_date} in hospital: {tenant_schema_name}")
    
    with schema_context(tenant_schema_name):
        title = "🌅 Today's Appointment Schedule"
        message = f"Good morning! The automated morning check for {current_date} has started. Preparing and sending schedules to doctors and patients."
        
        send_global_notification(
            tenant_schema=tenant_schema_name, 
            title=title, 
            message=message
        )
        
    logger.info(f"✅ Daily morning reminders completed for {tenant_schema_name}")
    return f"Daily morning reminders completed for {tenant_schema_name}"


@shared_task
def send_hourly_upcoming_reminders(tenant_schema_name):
    current_time = timezone.now()
    one_hour_later = current_time + timedelta(hours=1)
    formatted_time = one_hour_later.strftime('%H:%M')
    
    logger.info(f"⏱️ [Interval] Starting hourly check for critical upcoming appointments at {formatted_time} for hospital: {tenant_schema_name}")
    
    with schema_context(tenant_schema_name):
        title = "⏱️ Upcoming Appointment Reminder"
        message = f"Automated hourly alert: Important appointments are scheduled to start by {formatted_time}. Notifying relevant parties 1 hour in advance."
        
        send_global_notification(
            tenant_schema=tenant_schema_name, 
            title=title, 
            message=message
        )
        
    logger.info(f"✅ Hourly critical appointment check completed for {tenant_schema_name}")
    return f"Hourly reminders completed for {tenant_schema_name}"