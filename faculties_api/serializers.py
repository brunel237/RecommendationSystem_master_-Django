from django.forms import ValidationError
from rest_framework import serializers
from .models import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            'faculty_of',
            'dean',
        ]