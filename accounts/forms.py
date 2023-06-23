from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Patient, Doctor
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class PatientSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        patient = Patient.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    

class DoctorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    bmdc_number = forms.IntegerField()
    # bio = forms.Textarea()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        doctor = Doctor.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), bmdc_number=self.cleaned_data.get('bmdc_number'))
        return user

class DoctorProfileForm(UserCreationForm):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_profile')
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    bmdc_number = forms.IntegerField()
    bio = forms.Textarea()
    avatar = forms.ImageField()
    CHOICES = (
        ('gen-phy', 'General Physician'),
        ('derma', 'Dermatology'),
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
    L_CHOICES = (
        ('ctg', 'Chittagong'),
        ('dhaka', 'Dhaka'),
    )

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

    # speciality = forms.MultipleChoiceField(widget=)


    speciality = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxInput()
    )
    phone_number = forms.IntegerField()


    # email = forms.EmailField(widget=forms.EmailInput())
    
    experience = forms.IntegerField()
    # phone = 
    consultation_fee =forms.FloatField() 
    consultation_time_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    consultation_time_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    location = forms.MultipleChoiceField(
        choices=L_CHOICES,
        widget=forms.CheckboxInput()
    )
    hospital = forms.MultipleChoiceField(
        choices=H_CHOICES,
        widget=forms.CheckboxInput()
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        doctor = Doctor.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), bio=self.cleaned_data.get('bio'), bmdc_number=self.cleaned_data.get('bmdc_number'), speciality=self.cleaned_data.get('speciality'), phone_number=self.cleaned_data.get('phone_number'), consultation_fee=self.cleaned_data.get('consultation_fee'), experience = self.cleaned_data.get('experience'), consultation_time_start = self.cleaned_data.get('consultation_time_start'), consultation_time_end = self.cleaned_data.get('consultation_time_end'), location = self.cleaned_data.get('location'), hospital = self.cleaned_data.get('hospital'), avatar = self.cleaned_data.get('avatar') )
        return user

class PatientProfileForm(UserCreationForm):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_profile')
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    nickname = forms.CharField(widget=forms.TextInput())
    district = forms.CharField(widget=forms.TextInput())

    CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', "Other"),
    )

    # # speciality = forms.MultipleChoiceField(widget=)


    gender = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxInput()
    )
    phone_number = forms.IntegerField()
    age = forms.IntegerField()


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        patient = Patient.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), phone_number=self.cleaned_data.get('phone_number'), age = self.cleaned_data.get('age'), district = self.cleaned_data.get('district'), gender = self.cleaned_data.get('gender'), nickname = self.cleaned_data.get('nickname'))
        return user




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
