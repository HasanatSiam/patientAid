from django.urls import path
from . import views

urlpatterns = [
    path('d_profile/', views.profile),
]
