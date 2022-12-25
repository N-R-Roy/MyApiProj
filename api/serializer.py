from rest_framework import serializers
from myapp.models import StudentInfo, EmployeeInfo, UserInfo


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

