# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    nickname = models.CharField(max_length=100, default="")
    CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = 'male'
        )
    district = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

class Doctor(models.Model):

    CHOICES = (
        ('gen-phy', 'General Physician'),
        ('derma', 'Dermatology'),
        ('Pediatrics', 'Pediatrics'),
        ('dentist', "Dentistry"),
        ('gynecology', "Gynecology"),
        ('ophthalmology', "Ophthalmology"),
        ('neurology', "Neurology"),
        ('psychology', "Psychology"),
        ('orthopedics', "Orthopedics"),
        ('cardiology', "Cardiology"),
        ('gastroenterology', "Gastroenterology"),
        ('ent', "ENT"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    bmdc_number = models.IntegerField(null=True)

    speciality = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = ''
        )
    bio = models.TextField(null=True, default="MY bio")
    phone_number = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    experience = models.IntegerField(null=True)
    consultation_fee = models.FloatField(null=True)
    consultation_time_start = models.TimeField(null=True)
    consultation_time_end = models.TimeField(null=True)
    L_CHOICES = (
        ('ctg', 'Chittagong'),
        ('dhaka', 'Dhaka'),
    )
    location = models.CharField(
        max_length = 20,
        choices = L_CHOICES,
        default = 'dhaka'
        )
    
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')
    
    H_CHOICES = (
        ('national', 'National Hospital'),
        ('evercare', 'Evercare Hospital'),
        ('islami', 'Islami Bank Hospital'),
        ('memon', "Memon Maternity Hospital"),
        ('ctg-edical', "Chittagong Medical College Hospital"),
        ('square', "Square Hospital"),
        ('popular', "Popular Diagnostic Centre Ltd"),
        ('labaid', "Labaid Hospitals"),
        ('ibn-ina', "Ibn Sina Specialized Hospital"),
    
    )
    hospital = models.CharField(
        max_length = 30,
        choices = H_CHOICES,
        default = 'national'
        )
    like_count = models.IntegerField(default=0, null=True)
    dislike_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.user.id) + "--" + self.first_name + self.last_name
    
    # @property
    # def get_consultation_time_start(self):
    #     return str(self.consultation_time_start)
    


# class DoctorProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_profile')
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     bmdc_number = models.IntegerField(null=True)

#     bio = models.TextField(null=True, default="MY bio")

#     email = models.EmailField(unique=True)
    # specialty = 
    # experience = 
    # phone = 
    # consultation_fee = 
    # consultation_time = 
    # location = 
    # hospital = 


