from django import forms
from django.contrib.auth.models import Group


class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'permissions': forms.CheckboxSelectMultiple(),
        }
