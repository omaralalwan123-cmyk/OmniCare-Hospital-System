from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # نضع 'doctor' بدلاً من 'doctor_name'
    list_display = ('patient', 'doctor', 'appointment_date', 'status')
    list_filter = ('status', 'appointment_date', 'doctor')
    search_fields = ('patient__first_name', 'doctor__first_name', 'reason')