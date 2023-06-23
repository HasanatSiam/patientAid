from django.contrib import admin

# Register your models here.

# Register your models here.
# from accounts.models import User, Patient, Doctor

# admin.site.register(User)
# admin.site.register(Patient)

from .models import BookAppointment
admin.site.register(BookAppointment)