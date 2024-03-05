from django.db import models
from faculties_api.models import *

class Department(models.Model):
    department_of = models.CharField(unique=True, max_length=255)
    hod = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class DepartmentWithFaculty(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        abstract = True
