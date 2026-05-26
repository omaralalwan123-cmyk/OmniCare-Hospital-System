from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Hospital(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # إنشاء السكيما تلقائياً عند إضافة مستشفى جديد
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass