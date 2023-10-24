from django.db import models
from users_api.models import User
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    media = models.FileField( blank=True, null=True)
    




