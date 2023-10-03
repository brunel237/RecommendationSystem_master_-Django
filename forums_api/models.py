from django.db import models
from messages_api.models import *

class Forum(models.Model):
    name = models.CharField(max_length=255, unique=True)
    purpose = models.CharField(max_length=255)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name="participants_forum")
    
    

