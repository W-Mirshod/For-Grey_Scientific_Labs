from rest_framework import generics

from departments.models import Departments, Doctors, Patients
from departments.permissions import IsDoctorInSameDepartment
from departments.serializers import DepartmentSerializer


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()


class DepartmentDoctorsView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsDoctorInSameDepartment]
    lookup_field = 'slug'

    def get_queryset(self):
        doctors = Doctors.objects.all()
        return Departments.objects.filter(doctor_department__in=doctors)


class DepartmentPatientsView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsDoctorInSameDepartment]
    lookup_field = 'slug'

    def get_queryset(self):
        patients = Patients.objects.all()
        return Departments.objects.filter(patient_department__in=patients)
