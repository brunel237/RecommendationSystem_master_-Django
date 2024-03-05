from django.db import models
from messages_api.models import *

class Forum(models.Model):
    name = models.CharField(max_length=255, unique=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name="participants_forum")
    messages = models.ManyToManyField(Message, related_name="forum_messages")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_members(self):
        return self.participants.all()

    def add_member(self, member):
        try:
            self.participants.add(member)
            return 'ok'
        except Exception as e:
            return str(e)
        

    def remove_member(self, member):
        try:
            self.participants.remove(member)
            return 'ok'
        except Exception as e:
            return str(e)

    
    def number_of_participants(self):
        return self.participants.count()
    
    def get_discussions(self):
        return self.messages.all()
    
    def delete_message(self, message):
        try:
            msg = self.messages.get(message)
            self.messages.remove(message)
            msg.delete()
            return 'ok'
        except Exception as e:
            return str(e)
    
    def delete_forum(self):
        messages = self.messages.all()
        messages.delete()
        self.delete()

