from rest_framework import serializers
from django.contrib.auth.models import User
from exam.serializers import CourseSerializer, BatchSerializer

from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    #nested course and batch serializers ke liye
    # course_name = CourseSerializer(read_only=True)
    # batch = BatchSerializer(read_only=True)

    course_name = serializers.CharField(source='course_name.course_name', read_only=True)
    batch = serializers.CharField(source='batch.batch_name', read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'username', 'first_name', 'middle_name', 'last_name', 'batch', 'phone_number', 'course_name']

