from django.contrib import admin

# Register your models here.
from accounts.models import User, Patient, Doctor

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)