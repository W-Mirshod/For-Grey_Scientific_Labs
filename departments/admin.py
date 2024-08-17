from django.contrib import admin
from django.contrib.auth.models import Group
from departments.forms import CustomGroupForm

from django.contrib.auth.admin import GroupAdmin


# Register your models here.


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
