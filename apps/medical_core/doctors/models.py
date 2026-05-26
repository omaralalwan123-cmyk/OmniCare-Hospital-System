from django.db import models

class Doctor(models.Model):
    SPECIALTY_CHOICES = [
        ('general', 'General Practice'),
        ('cardiology', 'Cardiology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('dermatology', 'Dermatology'),
        ('neurology', 'Neurology'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50, choices=SPECIALTY_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.get_specialty_display()})"