from django.forms import ValidationError
from rest_framework import serializers
from .models import *
from faculties_api.serializers import FacultySerializer

class DepartmentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(required=True)

    class Meta:
        model = Department
        fields = [
            'department_of',
            'hod',
            'faculty'
        ]