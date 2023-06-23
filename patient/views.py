from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth import User
from accounts.models import Doctor, Patient
from .models import BookAppointment
# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse


doc_list = [
    {'id': 1, 'name': 'Dr. Faysal Rana', 'specialities': 'General Physician', 'hospital': 'Upazilla Health Complex,Faridganj', 'exp': 4},
    {'id': 2, 'name': 'Dr. Md. Mahbubul Islam', 'specialities': 'General Physician', 'hospital': 'Shaheed Suhrawardy Medical College Hospital, Dhaka', 'exp': 10},
    {'id': 3, 'name': 'Md Meraz Hossain', 'specialities': 'Psychologist', 'hospital': 'Bangladesh Institute of Graphology, ', 'exp': 11},
    {'id': 4, 'name': 'Md Meraz Hossain', 'specialities': 'Psychologist', 'hospital': 'Bangladesh Institute of Graphology, ', 'exp': 11},
    {'id': 5, 'name': 'Md Meraz Hossain', 'specialities': 'Psychologist', 'hospital': 'Bangladesh Institute of Graphology, ', 'exp': 11},
]


def services(request):
    return render(request, 'patient/services.html')

# def prediction(request):
#     return render(request, 'patient/prediction.html')

def profile(request):
    return render(request, 'patient/patient_profile.html')

from django.core.paginator import Paginator
def doctor_list(request, speciality):
    # context = {'doc_list': doc_list}
    doctors = Doctor.objects.filter(speciality=speciality)
    paginator = Paginator(doctors, 4)  # Show 10 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'patient/doctor_list.html', {'doctors': doctors, 'page_obj': page_obj})

from django.contrib.auth import get_user_model
def doctor_view(request, id):
    user_model = get_user_model()
    user = user_model.objects.get(id=id)
    doc = Doctor.objects.get(user=user)

    return render(request, 'patient/doctor_view.html', {'doc': doc})


def like(request, id):
    user_model = get_user_model()
    user = user_model.objects.get(id=id)
    doc = Doctor.objects.get(user=user)
    doc.like_count = doc.like_count + 1
    doc.save()
    return render(request, 'patient/doctor_view.html', {'doc': doc})



from django.contrib import messages
def book_appointment(request, doctor_id):

    user_model = get_user_model()
    user = user_model.objects.get(id=doctor_id)
    doctor = Doctor.objects.get(user=user)
    patient = Patient.objects.get(user=request.user)
    print("------START----------")
    if request.method == 'POST':
        print("------POSSSSST---")
        appointment_date = request.POST.get('appointment_date')
        # appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')

        app_count = BookAppointment.objects.filter(doctor=doctor, appointment_date=appointment_date).count() + 1
        print(app_count)
        if app_count > 12:
            messages.error(request, 'Failed to book the appointment, select another date')
            return render(request, 'patient/app.html', {'doc': doctor})

        app = BookAppointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_date=appointment_date,
            reason=reason
        )

        total_app = BookAppointment.objects.filter(doctor=doctor, appointment_date=app.appointment_date).count()
        print('Total app -----> ', total_app)
        serial = total_app + 1
        app.serial = serial
        # app.save()
        # try:
        app.save()
        messages.success(request, 'Appointment booked successfully!')
        # url = reverse('view_appointment',  kwargs={'app_id': app.id})
        return redirect('view_appointment', app.id)  # Redirect to a success page
            
        # except:
        #     messages.error(request, 'Failed to book the appointment. Please try again.')
        #     return redirect('doctor-view')


        return render(request, 'patient/doctor_view.html', {'doc': doctor})
    return render(request, 'patient/app.html', {'doc': doctor})


def view_appointment(request, app_id):
    print("#########################")
    # user_model = get_user_model()
    # user = user_model.objects.get(id=doctor_id)
    # doctor = Doctor.objects.get(user=user)
    patient = Patient.objects.get(user=request.user)
    app = BookAppointment.objects.get(id=app_id)
    apps = BookAppointment.objects.filter(patient=patient).order_by('-appointment_date')
    total_app = BookAppointment.objects.filter(doctor=app.doctor, appointment_date=app.appointment_date).count()
    serial = total_app + 1
    # serial = 2222
    return render(request, 'patient/view_app.html', {'apps': apps, 'serial': serial})


def view_appointment_all(request):
    patient = Patient.objects.get(user=request.user)
    apps = BookAppointment.objects.filter(patient=patient).order_by('-appointment_date')
    return render(request, 'patient/view_app_all.html', {'apps': apps})


        
def embed(request):
    return render(request, 'patient/embed.html')






