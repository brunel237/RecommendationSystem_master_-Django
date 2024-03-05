from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *
from courses_api.models import AcademicLevelCourse
from PIL import Image
import os


def handle_image(name, profile_picture, path):
    filename = f"{name}-profile.png"
    file_path = 'resources/'+path+filename
    image = Image.open(profile_picture)
    image = image.resize((200, 200))
    image.save(file_path)
    return path+filename

class UserSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(min_length=6)
    email = serializers.EmailField()
    date_of_birth = serializers.DateField()
    # profile_picture = serializers.FileField(allow_null=True)
    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'first_name',
            'last_name',
            'username',
            'email',
            'sex',
            'date_of_birth',
            'registration_number',
            'phone_number',
            'address',
            'status',
            'profile_picture',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    
    def retrieve(self, validated_data, pk=None):
        user = get_object_or_404(Lecturer.objects.select_related('user'), user=pk)
        user = LecturerSerializer(user)
        return user.data

    def create(self, validated_data):
        profile_picture = validated_data.get('profile_picture')
        if profile_picture:
            validated_data["profile_picture"] = handle_image(validated_data["username"], profile_picture, 'profile/profile_pics/')
        else:
            validated_data["profile_picture"] = 'profile/profile_pics/profile_default.png'

        password = validated_data.pop('password')
        validated_data["password"] = make_password(password)
        user = User.objects.create(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

    # def update(self, instance, validated_data):
    #     if 'password' in validated_data:
    #         password = validated_data.pop('password')
    #         instance.set_password(password)
    #     if instance.status=="student":
    #         Student.objects.update(user=instance, **validated_data)
    #     elif instance.status=="school_elder":
    #         SchoolElder.objects.update(user=instance, **validated_data)
    #     else:
    #         Lecturer.objects.update(user=instance, **validated_data)
    #     return super().update(instance, validated_data)


# class AcademicLevelCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AcademicLevelCourse
#         fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    courses_attending = serializers.PrimaryKeyRelatedField(queryset=AcademicLevelCourse.objects.all(), many=True, required=False)
    class Meta:
        model = Student
        fields = [
            'user',
            'courses_attending',
        ]

    def create(self, validated_data):
        courses_attending = validated_data.pop('courses_attending')
        student = Student.objects.create(**validated_data)
        student.courses_attending.set(courses_attending)
        return student

    def update(self, instance, validated_data):
        
        if "courses_attending" in validated_data:
            courses_attending = validated_data.pop('courses_attending')
        
            if instance.courses_attending.exists():
                temp = instance.courses_attending.all()
                
                for item in temp:
                    courses_attending.append(item.id)
                    
            instance.courses_attending.set(courses_attending)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance


class SchoolElderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    followers = UserSerializer(many=True)
    courses_attending = serializers.PrimaryKeyRelatedField(queryset=AcademicLevelCourse.objects.all(), many=True, required=False)

    class Meta:
        model = SchoolElder
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['user'] = representation['user']['id']  # Replace user object with user ID
    #     return representation

    def create(self, validated_data):
        courses_attending = validated_data.pop('courses_attending')
        se = SchoolElder.objects.create(**validated_data)
        se.courses_attending.set(courses_attending)
        return se

    def update(self, instance, validated_data):
        
        if "courses_attending" in validated_data:
            courses_attending = validated_data.pop('courses_attending')
            if  len(courses_attending) == 0 :
                instance.courses_attending.clear()
            
            elif instance.courses_attending.exists():
                temp = instance.courses_attending.all()
                
                for item in temp:
                    courses_attending.append(item.id)
                    
            instance.courses_attending.set(courses_attending)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance


class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    lectures = serializers.PrimaryKeyRelatedField(queryset=AcademicLevelCourse.objects.all(), many=True, required=False)
    followers = UserSerializer(many=True)
    
    class Meta:
        model = Lecturer
        fields = '__all__'
    
    def get_serialized_lecturer(self, user):
        return get_object_or_404(Lecturer.objects.select_related('user'), user=user)


    def create(self, validated_data):
        lectures = validated_data.pop('lectures')
        lecturer = Lecturer.objects.create(**validated_data)
        lecturer.lectures.set(lectures)
        return lecturer
    
    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user', {})
    #     lectures = validated_data.pop('lectures', None)
    #     user = instance.user
    #     if lectures is not None:
    #         instance.lectures.set(lectures)
    #     if user_data:
    #         for attr, value in user_data.items():
    #             setattr(user, attr, value)
    #         if 'password' in user_data:
    #             user.set_password(user_data['password'])
    #         user.save()
    #     return super().update(instance, validated_data)


