from django.forms import ValidationError
from rest_framework import serializers
from .models import *



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOfStudy
        fields = [
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