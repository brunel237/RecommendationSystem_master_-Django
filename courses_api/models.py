from django.db import models
from departments_api.models import *

class AcademicLevel(models.Model):
    LEVEL_CHOICES = [
        ("l1", "Level 1"),
        ("l2", "Level 2"),
        ("l3", "Level 3"),
        ("m1", "Master 1"),
        ("m2", "Master 2"),
        ("predoc", "Pre Doctorate"),
    ]
    
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
 
class CourseOfStudy(models.Model):
    course_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    course_name = models.CharField(max_length=255)
    is_research_field = models.BooleanField(default=False)
    description = models.TextField(blank=True, max_length=255)

class AcademicLevelCourse(models.Model):
    level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseOfStudy, on_delete=models.CASCADE)

class AcademicLevelWithDepartment(models.Model):
    level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class CourseOfStudyWithAcademicLevel(models.Model):
    course = models.ForeignKey(CourseOfStudy, on_delete=models.CASCADE)
    academic_level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE)

    class Meta:
        abstract = True

# Create your models here.
