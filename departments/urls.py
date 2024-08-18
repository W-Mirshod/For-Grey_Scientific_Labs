from django.urls import path

from departments.views.doctors import DoctorsList, DoctorDetail
from departments.views.patients import PatientsList, PatientDetail

urlpatterns = [
    # doctors
    path('doctors/', DoctorsList.as_view(), name='doctors'),
    path('doctors/<int:doctor_id>', DoctorDetail, name='doctor_detail'),

    # patients
    path('patients/', PatientsList.as_view(), name='patients'),
    path('patients/<int:patient_id>', PatientDetail, name='patient_detail'),
]
