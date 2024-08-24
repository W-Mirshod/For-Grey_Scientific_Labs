from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from departments.views.departments import DepartmentView, DepartmentDoctorsView, DepartmentPatientsView
from departments.views.doctors import DoctorsList, DoctorDetail
from departments.views.patient_records import PatientRecordsView, patient_records_detail
from departments.views.patients import PatientsList, patient_detail
from departments.views.views import DepartmentViewSet, PatientViewSet, DoctorViewSet, PatientRecordViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patient-records', PatientRecordViewSet)

urlpatterns = [
                  path('', include(router.urls)),
                  # doctors
                  path('doctors/', DoctorsList.as_view(), name='doctors'),
                  path('doctors/<int:doctor_id>/', DoctorDetail, name='doctor_detail'),

                  # patients
                  path('patients/', PatientsList.as_view(), name='patients'),
                  path('patients/<int:patient_id>/', patient_detail, name='patient_detail'),

                  # patient_records
                  path('patient-records/', PatientRecordsView.as_view(), name='patient_records'),
                  path('patient-records/<slug:pr_slug>/', patient_records_detail, name='patient_records_details'),

                  # departments
                  path('departments/', DepartmentView.as_view(), name='departments'),
                  path('departments/<slug:slug>/doctors', DepartmentDoctorsView.as_view(), name='doctor_department'),
                  path('departments/<slug:slug>/patients', DepartmentPatientsView.as_view(), name='patient_department'),
              ] + debug_toolbar_urls()
