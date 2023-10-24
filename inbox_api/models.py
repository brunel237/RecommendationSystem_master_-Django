from django.db import models
from messages_api.models import *

class Inbox(models.Model):
    owner = models.ForeignKey(User, related_name="inbox_owner", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, related_name="inbox_guest", on_delete=models.CASCADE)
    messages = models.ManyToManyField(Message, related_name="inbox_messages")
    hidden = models.BooleanField(default=False)
    
    def get_discussions(self):
        return self.messages.all()
    
    def delete_message(self, message):
        try:
            self.messages.remove(message)
            message.delete()
            return True
        except Exception as e:
            return str(e)

    def get_inbox(owner, guest):
        inboxes = Inbox.objects.all()
        for inbox in inboxes:
            if (inbox.owner==guest and inbox.guest==owner) or (inbox.owner==owner and inbox.guest==guest):
                return inbox
        inbox = Inbox.objects.create(owner=owner, guest=guest)
        return inbox

    def hide_message(self, message):
        if message in self.messages.all():
            message.hidden = True
            message.save()

    def hide_inbox(self):
        self.hidden = True
        self.save()

    def get_visible_messages(self, user):
        if user == self.owner:
            return self.messages.all()
        else:
            return self.messages.filter(hidden=False)

