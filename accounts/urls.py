from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient_home, name="patient-home"),
    # path("", views.doctor_home, name="doctor-home"),
    path("doctor/", views.doctor_home, name="doctor-home"),
    path("doctor/edit/", views.doctor_profile_update, name="doctor-update"),
    path("doctor/view/", views.doctor_profile, name="doctor-profile"),

    path("patient/edit/", views.patient_profile_update, name="patient-update"),
    path("patient/view/", views.patient_profile, name="patient-profile"),


    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("signup/patient/", views.PatientSignUpView.as_view(), name="patient-signup"),
    path("signup/doctor/", views.DoctorSignUpView.as_view(), name="doctor-signup"),
]

