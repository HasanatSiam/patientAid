from django.db import models

# Create your models here.
from accounts.models import Doctor, Patient

# class BookAppointment(models.Model):
#     date = models.DateField()
#     doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, primary_key=True, related_name='doctor')

#     doctor = models.ManyToManyField()


class BookAppointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    # appointment_time = models.TimeField()
    reason = models.TextField()
    serial = models.IntegerField(default=0)

    # def __str__(self):
    #     return f"{self.patient.name} - {self.doctor.name} -{self.appointment_date}"