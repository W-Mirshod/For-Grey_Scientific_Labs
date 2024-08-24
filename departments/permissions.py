from rest_framework import permissions

from departments.models import Departments, Patients, Doctors


class IsDoctor(permissions.BasePermission):
    message = 'You do not have permission to enter this page.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='Doctors').exists():
                return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsOwnProfile(permissions.BasePermission):
    message = 'You do not have permission to enter this page.'

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user == request.user:
            if request.user.groups.filter(name='Doctors').exists():
                return request.user
        return False

    def has_object_permission(self, request, view, obj):
        if self.has_permission(request, view) and request.user == obj:
            return True
        return False


class IsPatient(permissions.BasePermission):
    message = 'You do not have permission to enter this page.'

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user == request.user:
            if request.user.groups.filter(name='Patients').exists():
                return request.user
        return False

    def has_object_permission(self, request, view, obj):
        if self.has_permission(request, view) and request.user == obj:
            return True
        return False


class IsRelevantDoctor(permissions.BasePermission):
    message = 'You do not have permission to enter this page.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='Doctors').exists():
                return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsDoctorInSameDepartment(permissions.BasePermission):
    message = 'You do not have permission to enter this page.'

    def has_permission(self, request, view):
        patients = Patients.objects.all()
        doctors = Doctors.objects.all()
        return Departments.objects.filter(patient_department__in=patients).exists() or Departments.objects.filter(
            doctor_department__in=doctors).exists()


class IsRelevantPatientOrDoctor(permissions.BasePermission):
    message = 'You do not have permission to enter this page.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='Doctors').exists() or request.user.groups.filter(
                    name='Patients').exists():
                return True
        return False
