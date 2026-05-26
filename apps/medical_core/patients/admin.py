from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # الحقول التي ستظهر في القائمة الرئيسية
    list_display = ('first_name', 'last_name', 'phone_number', 'created_at')
    
    # إضافة خاصية البحث بالاسم أو رقم الهاتف
    search_fields = ('first_name', 'last_name', 'phone_number')
    
    # إضافة فلاتر جانبية (مثلاً حسب تاريخ الإضافة)
    list_filter = ('created_at', 'gender')