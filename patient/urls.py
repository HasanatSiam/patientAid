from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name="patient-home"),
    path('list/<str:speciality>', views.doctor_list, name='list'),
    path('doctor/view/<int:id>', views.doctor_view, name='doctor-view'),
    path('doctor/like/<int:id>', views.like, name='doctor-like'),
    path('book/appointemt/doctor/<int:doctor_id>', views.book_appointment, name='book_appointment'),
    path('appointemt/view/<int:app_id>', views.view_appointment, name='view_appointment'),
    path('appointemt/view/all', views.view_appointment_all, name='view_appointment_all'),
    path('patient/embed', views.embed, name='embed'),
    # path('patient/prediction', views.prediction, name='prediction'),

    path('profile/', views.profile),
]
