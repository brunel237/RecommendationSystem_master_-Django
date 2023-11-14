from django.forms import ValidationError
from rest_framework import serializers
from .models import *
from departments_api.serializers import *



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOfStudy
        fields = [
            'id',
            'course_code',
            'course_name',
            'is_research_field',
            'description',
        ]
        
    def create(self, validated_data):
        course_code = validated_data['course_code']
        if len(course_code) < 6:
            raise ValidationError({'message': 'Course Code must be at least 6 characters'})
        course = CourseOfStudy.objects.create(**validated_data)
        return course

class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'

class AcademicLevelCourseSerializer(serializers.ModelSerializer):
    level = AcademicLevelSerializer()
    department = DepartmentSerializer()
    course = CourseSerializer()
    class Meta:
        model = AcademicLevelCourse
        fields = '__all__'
    
    