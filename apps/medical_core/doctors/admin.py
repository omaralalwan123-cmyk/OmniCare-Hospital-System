from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'license_number', 'is_active')
    list_filter = ('specialty', 'is_active')
    search_fields = ('first_name', 'last_name', 'license_number')