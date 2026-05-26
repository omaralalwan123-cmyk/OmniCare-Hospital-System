from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        verbose_name="Gender"
    )
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    medical_history = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Medical History"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"