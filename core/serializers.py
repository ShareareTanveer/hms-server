from rest_framework import serializers
from django.contrib.auth import get_user_model
from authentication.serializers import SimpleUserCreateSerializer, UserCreateSerializer
from .models import UserDetail, Employee, Notice, AppSettings

User = get_user_model()


class UserDetailByUserIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class SimpleUserDetailSerializer(serializers.ModelSerializer):
    user = SimpleUserCreateSerializer()

    class Meta:
        model = UserDetail
        fields = ['id', 'address', 'phone',
                  'blood_group', 'date_of_birth', 'sex', 'user']


class PostUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id', 'address', 'phone',
                  'blood_group', 'date_of_birth', 'sex', 'user']


class UserDetailSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = UserDetail
        fields = ['id', 'address', 'phone',
                  'blood_group', 'date_of_birth', 'sex', 'user']


class EmployeeSerializer(serializers.ModelSerializer):
    user_details = UserDetailSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user_details', 'status']

    def create(self, validated_data):
        emp_data = validated_data.copy()
        user_details_data = emp_data.pop('user_details')
        user_data = user_details_data.pop('user')
        user = User.objects.create(**user_data)
        user_details = UserDetail.objects.create(
            user=user, **user_details_data)
        emp = Employee.objects.create(user_details=user_details, **emp_data)
        return emp


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'description', 'start_date', 'end_date', 'status']


class AppSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSettings
        fields = '__all__'
