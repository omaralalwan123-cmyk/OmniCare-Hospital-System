from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Hospital, Domain

@admin.register(Hospital)
class HospitalAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'schema_name', 'created_on')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant')