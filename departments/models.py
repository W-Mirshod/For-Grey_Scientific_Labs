from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.text import slugify


class Departments(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    diagnostics = models.TextField()
    location = models.CharField(max_length=250, null=True, blank=True)
    specialization = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.name)}-{i}"
                if not Departments.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Departments, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Departments'


class Patients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_user')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='patient_department')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.department.name}"

    class Meta:
        verbose_name_plural = 'Patients'


class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_user')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='doctor_department')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.department}"

    class Meta:
        verbose_name_plural = 'Doctors'


class PatientRecords(models.Model):
    record_id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, blank=True)
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_records')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    diagnostics = models.TextField()
    observations = models.TextField(null=True, blank=True)
    treatment = models.TextField()
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    misc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.patient_id.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.patient_id.username)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.patient_id.username)}-{i}"
                if not PatientRecords.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(PatientRecords, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Patient Records'
