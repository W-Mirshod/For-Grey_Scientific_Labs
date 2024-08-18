from rest_framework import permissions

from departments.models import PatientRecords


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
            print(1)
            return True
        return False


# class IsOwnProfile(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj == request.user


class IsRelevantDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.department.doctor == request.user


class IsDoctorInSameDepartment(permissions.BasePermission):
    def has_permission(self, request, view):
        return PatientRecords.objects.filter(department__doctor=request.user).exists()


class IsRelevantPatientOrDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Patients').exists():
            return obj.patient == request.user
        elif request.user.groups.filter(name='Doctors').exists():
            return obj.department.doctor == request.user
        return False
