from django.db import models


class Faculty(models.Model):
    faculty_of = models.CharField(unique=True, max_length=255)
    dean = models.CharField(max_length=255)
    

