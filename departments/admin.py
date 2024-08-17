from django.contrib import admin
from django.contrib.auth.models import Group
from departments.models import PatientRecords, Departments
from departments.forms import CustomGroupForm

from django.contrib.auth.admin import GroupAdmin


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)


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
