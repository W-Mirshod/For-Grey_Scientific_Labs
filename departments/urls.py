from django.urls import path

from departments.views import DoctorsList, DoctorDetail

urlpatterns = [
    path('doctors/', DoctorsList.as_view(), name='doctors'),
    path('doctors/<int:doctor_id>', DoctorDetail, name='doctor_detail'),
]
