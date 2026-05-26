from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.medical_core.patients.models import Patient
from apps.medical_core.doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)

    def clean(self):
        # 1. Prevent past appointments
        if self.appointment_date and self.appointment_date < timezone.now():
            raise ValidationError("Error: You cannot schedule an appointment in the past.")

        # 2. Prevent overlapping appointments for the same doctor
        # We check if another scheduled appointment exists at the exact same time
        conflicting_appointments = Appointment.objects.filter(
            doctor=self.doctor,
            appointment_date=self.appointment_date,
            status='scheduled'
        ).exclude(pk=self.pk)

        if conflicting_appointments.exists():
            raise ValidationError(
                f"Conflict: Dr. {self.doctor} already has another appointment at this specific time."
            )

    def save(self, *args, **kwargs):
        # Explicitly call full_clean to trigger validation before saving
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient} - {self.doctor} ({self.appointment_date})"