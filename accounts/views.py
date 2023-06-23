# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# def login(request):
#     return render(request, 'accounts/login.html')

# def register(request):
#     form = UserCreationForm()
#     context = {'form':form}
#     return render(request, 'accounts/register.html')


from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.urls import reverse

from .models import User, Doctor, Patient
from .forms import PatientSignUpForm, DoctorSignUpForm, LoginForm, DoctorProfileForm, PatientProfileForm
from django.contrib.auth import get_user
from django.urls import reverse_lazy

from django.contrib.auth import authenticate 
# def register(request):
#     if request.method == 'POST':
#         form = PatientCreationForm(request.POST)
#         if form.is_valid():
#             patient = form.save()
#             login(request, patient)
#             return redirect('home')  # Replace 'home' with the appropriate URL for the home page
#     else:
#         form = PatientCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})

# def doctor_signup(request):
#     if request.method == 'POST':
#         form = DoctorCreationForm(request.POST)
#         if form.is_valid():
#             doctor = form.save()
#             login(request, doctor)
#             return redirect('home')  # Replace 'home' with the appropriate URL for the home page
#     else:
#         form = DoctorCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'accounts/patient_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient-home')
    

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'accounts/doctor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor-home')
    

# class DoctorProfileView(CreateView):
#     model = User
#     form_class = DoctorProfileForm
#     template_name = 'accounts/doctor_signup.html'

#     # def get_context_data(self, **kwargs):
#     #     kwargs['user_type'] = 'doctor'
#     #     return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('doctor-home')
    

def doctor_profile_update(request):
    # doctor = User.objects.get(id=id, is_doctor=True)
    # doctor = Doctor.objects.get(user=request.user)
    # user = User.objects.get(id=id)
    # doctor = Doctor.objects.get(user=user)
    user = get_user(request)
    print(user)
    doctor = Doctor.objects.get(user=user)



    if request.method == 'POST':
        bmdc_number = request.POST.get('bmdc_number', "")
        phone_number = request.POST.get('phone_number', "")
        bio = request.POST.get('bio', "")
        speciality = request.POST.get('speciality', "")
        experience = request.POST.get('experience', "")
        # phone = 
        consultation_fee = request.POST.get('consultation_fee', "")
        consultation_time_start = request.POST.get('consultation_time_start', "")
        consultation_time_end = request.POST.get('consultation_time_end', "")
        print(consultation_time_start, consultation_time_end)
        location = request.POST.get('location', "")
        hospital =  request.POST.get('hospital', "")
        avatar = request.FILES.get('avatar')

        doctor.bmdc_number = int(bmdc_number)
        doctor.phone_number = int(phone_number)
        doctor.bio = str(bio)
        doctor.speciality = str(speciality)
        doctor.experience = int(experience)
        doctor.consultation_fee = float(consultation_fee)
        doctor.consultation_time_start = consultation_time_start
        doctor.consultation_time_end = consultation_time_end
        doctor.location = str(location)
        doctor.hospital = str(hospital)
        doctor.avatar = avatar

        doctor.save()

        return redirect('doctor-profile')
    return render(request, 'accounts/doctor_profile.html', {'doctor': doctor})


def doctor_profile(request):
    user = get_user(request)
    print(user)
    doctor = Doctor.objects.get(user=user)

    return render(request, 'accounts/doctor_profile_view.html', {'doctor': doctor})


def patient_profile_update(request):
    # doctor = User.objects.get(id=id, is_doctor=True)
    # doctor = Doctor.objects.get(user=request.user)
    # user = User.objects.get(id=id)
    # patient = Patient.objects.get(user=user)
    user = get_user(request)
    print(user)
    patient = Patient.objects.get(user=user)


    if request.method == 'POST':
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        phone_number = request.POST.get('phone_number', "")
        age = request.POST.get('age', "")
        district = request.POST.get('district', "")
        nickname = request.POST.get('nickname', "")
        gender = request.POST.get('gender', "")

        patient.first_name = str(first_name)
        patient.last_name = str(last_name)
        patient.age = int(age)
        patient.district = str(district)
        patient.nickname = str(nickname)
        patient.gender = str(gender)
        patient.phone_number = int(phone_number)
        patient.save()

        return redirect('patient-profile')
    return render(request, 'accounts/patient_profile.html', {'patient': patient})

def patient_profile(request):
    user = get_user(request)
    print(user)
    patient = Patient.objects.get(user=user)
    print(patient)
    return render(request, 'accounts/patient_profile_view.html', {'patient': patient})

    

# class LoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'accounts/login.html'

#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)

#     def get_success_url(self):
#         user = self.request.user
#         if user.is_authenticated:
#             if user.is_patient:
#                 return reverse('patient-home')
#             elif user.is_doctor:
#                 return reverse('doctor-home')
#         else:
#             return reverse('login')


     
# def login_view(request):
#     print("login function")
#     form = LoginForm()
#     # if request.user.is_authenticated:
#     #     return redirect("doctor-update")
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         print(form.is_valid())
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )

#             if user is not None:
#                 login(request, user)
#                 message = f'Hello {user.username}! You have been logged in'
#             else:
#                 message = 'Login failed!'
#                 return reverse('login')
#     return render(request, 'accounts/login1.html', {'form': form})




class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login1.html' 


    def get_success_url(self):
        if self.request.user.is_doctor:
            return reverse_lazy('doctor-home')
        if self.request.user.is_patient:
            return reverse_lazy('patient-home')


def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'home' with the URL name of your home page


from django.http import HttpResponse
def patient_home(request):
    return redirect('patient:patient-home')


from patient.models import BookAppointment
def doctor_home(request):    
    # return HttpResponse("doctor-home:  " + str(request.user))
    # doctor_user = request.user

    # return redirect('doctor-home')
    user = get_user(request)
    print(user)
    doctor = Doctor.objects.get(user=user)
    app_all = BookAppointment.objects.filter(doctor=doctor)
    print(app_all)

    return render(request, 'accounts/doctor_home.html', {'app_all': app_all})




