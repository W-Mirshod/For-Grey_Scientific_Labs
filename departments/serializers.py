from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from departments.models import Departments, PatientRecords, Doctors, Patients


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorDetailSerializer(serializers.ModelSerializer):
    data = SerializerMethodField()

    def get_data(self, obj):
        return obj.data

    class Meta:
        model = Doctors
        fields = ['id', 'user', 'group']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class PatientRecordSerializer(serializers.ModelSerializer):
    department_id = serializers.SlugRelatedField(slug_field='slug', queryset=Departments.objects.all())

    class Meta:
        model = PatientRecords
        fields = ['record_id', 'patient_id', 'slug', 'department_id']


class PatientRecordDetailSerializer(serializers.ModelSerializer):
    department_id = serializers.SlugRelatedField(slug_field='slug', queryset=Departments.objects.all())

    class Meta:
        model = PatientRecords
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label='Confirm password')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, data):
#         user = User.objects.filter(username=data['username']).first()
#         if user is None or not user.check_password(data['password']):
#             raise serializers.ValidationError("Invalid username or password")
#         return data
#
#
# class DummySerializer(serializers.Serializer):
#     pass
