from typing import Any
from django.db import models
from users_api.models import *


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="message_receiver", on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    attached_file = models.FileField(blank=True, null=True, upload_to="chats/")
    hidden = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

 

