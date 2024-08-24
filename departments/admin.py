from django.contrib import admin
from django.contrib.auth.models import Group, User
from departments.models import PatientRecords, Departments, Doctors, Patients
from departments.forms import CustomGroupForm

from django.contrib.auth.admin import GroupAdmin

admin.site.unregister(Group)


# admin.site.unregister(User)


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm


admin.site.register(Group, CustomGroupAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(PatientRecords)
class PatientRecordsAdmin(admin.ModelAdmin):
    list_display = ['record_id', 'patient_id', 'slug', 'created_at', 'department_id']
    search_fields = ['record_id']
    list_filter = ['record_id', 'patient_id', 'created_at']
    exclude = ['slug']


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    search_fields = ['name']
    list_filter = ['id', 'name']
    exclude = ['slug']


@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'group']
    search_fields = ['user']
    list_filter = ['id', 'user']


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'group']
    search_fields = ['user']
    list_filter = ['id', 'user']
