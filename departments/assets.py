from django.contrib.auth.models import Group, User


def create_group():
    patients_group, created = Group.objects.get_or_create(name='Patients')
    doctors_group, created = Group.objects.get_or_create(name='Doctors')

    user_patient, created = User.objects.get_or_create(username='patient_user', defaults={'password': '123'})
    user_doctor, created = User.objects.get_or_create(username='doctor_user', defaults={'password': '123'})

    user_patient.groups.add(patients_group)
    user_doctor.groups.add(doctors_group)

    user_patient.save()
    user_doctor.save()


create_group()
