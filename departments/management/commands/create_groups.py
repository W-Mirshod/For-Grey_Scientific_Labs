from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create user groups for Patients and Doctors'

    def handle(self, *args, **kwargs):
        patients_group, created = Group.objects.get_or_create(name='Patients')

        doctors_group, created = Group.objects.get_or_create(name='Doctors')

        # Add permissions to groups if needed (optional)
        # For example, allow doctors to view and change patient records
        # content_type = ContentType.objects.get_for_model(Patient)
        # view_patient_perm = Permission.objects.get(
        #     codename='view_patient',
        #     content_type=content_type,
        # )
        # doctors_group.permissions.add(view_patient_perm)

        self.stdout.write(self.style.SUCCESS('Successfully created Patients and Doctors groups'))
