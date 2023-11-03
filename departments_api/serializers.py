from django.forms import ValidationError
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'department_of',
            'hod',
            'faculty'
        ]