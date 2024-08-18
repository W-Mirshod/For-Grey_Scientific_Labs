from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from departments.permissions import IsDoctor
from departments.serializers import PatientSerializer


class PatientsList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        patients_group = Group.objects.get(name='Patients')
        return User.objects.filter(groups=patients_group)


@api_view(['GET'])
@permission_classes([IsDoctor, IsAuthenticated])
def PatientDetail(request, patient_id):
    patient = get_object_or_404(User, id=patient_id)
    patients_group = Group.objects.get(name='Patients')
    if not patient.groups.filter(name=patients_group).exists():
        data = {'detail': 'Patient not found'}
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    print(request.user.groups)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
