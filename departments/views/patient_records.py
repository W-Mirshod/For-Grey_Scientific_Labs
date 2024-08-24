from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from departments.models import PatientRecords
from departments.permissions import IsRelevantDoctor, IsRelevantPatientOrDoctor
from departments.serializers import PatientRecordSerializer, PatientRecordDetailSerializer


class PatientRecordsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsRelevantDoctor)
    serializer_class = PatientRecordSerializer
    queryset = PatientRecords.objects.all()


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsRelevantPatientOrDoctor])
def patient_records_detail(request, pr_slug):
    patient_record = get_object_or_404(PatientRecords, slug=pr_slug)

    if request.method == 'GET':
        serializer = PatientRecordDetailSerializer(patient_record)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PatientRecordDetailSerializer(patient_record)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        patient_record = PatientRecords.objects.filter(slug=pr_slug)
        if patient_record:
            patient_record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
