from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from departments.models import Patients
from departments.permissions import IsDoctor, IsPatient
from departments.serializers import PatientSerializer


class PatientsList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        patients_group = Patients.objects.all()
        return patients_group


@api_view(['GET', 'POST'])
@permission_classes([IsDoctor, IsPatient, IsAuthenticated])
def patient_detail(request, patient_id):
    patient = get_object_or_404(User, id=patient_id)
    patients_group = Group.objects.get(name='Patients')
    if not patient.groups.filter(name=patients_group).exists():
        data = {'detail': 'Patient not found'}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        patient1 = patient.groups.filter(id=patient_id)
        if patient1:
            patient1.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
