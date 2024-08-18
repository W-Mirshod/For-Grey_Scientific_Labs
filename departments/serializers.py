from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.fields import SerializerMethodField

from departments.models import Departments, PatientRecords


class DoctorSerializer(serializers.ModelSerializer):
    groups = SerializerMethodField()
    email = SerializerMethodField()

    def get_groups(self, obj):
        obj_groups = obj.groups.all()
        groups = []
        for group in obj_groups:
            groups.append(group.name)
        if groups:
            return groups
        return None

    def get_email(self, obj):
        if obj.email:
            return obj.email
        return None

    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'email', 'date_joined']


class DoctorDetailSerializer(serializers.ModelSerializer):
    groups = SerializerMethodField()
    email = SerializerMethodField()

    def get_groups(self, obj):
        obj_groups = obj.groups.all()
        groups = []
        for group in obj_groups:
            groups.append(group.name)
        if groups:
            return groups
        return None

    def get_email(self, obj):
        if obj.email:
            return obj.email
        return None

    class Meta:
        model = User
        exclude = ['password', 'user_permissions']


class PatientSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), write_only=True)
    groups = SerializerMethodField()
    email = SerializerMethodField()

    def get_groups(self, obj):
        obj_groups = obj.groups.all()
        groups = []
        for group in obj_groups:
            groups.append(group.name)
        if groups:
            return groups
        return None

    def get_email(self, obj):
        if obj.email:
            return obj.email
        return None

    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'group', 'email', 'date_joined']

    def create(self, validated_data):
        group = validated_data.pop('group', None)
        user = super().create(validated_data)
        if group:
            user.groups.add(group)
        return user


class PatientRecordSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='slug', queryset=Departments.objects.all())

    class Meta:
        model = PatientRecords
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
