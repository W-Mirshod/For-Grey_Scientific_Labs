from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from departments.permissions import IsDoctor, IsOwnProfile
from departments.serializers import DoctorSerializer, DoctorDetailSerializer


class DoctorsList(APIView):
    permission_classes = (IsDoctor, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        patients_group = Group.objects.get(name='Doctors')
        doctors = User.objects.filter(groups=patients_group)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsOwnProfile, IsAuthenticated])
def DoctorDetail(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id)

    if request.user != doctor:
        data = {'detail': 'You do not have permission to access this resource.'}
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = DoctorDetailSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = DoctorDetailSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
