from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
# from messages_api.models import *


class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    class UserManager(BaseUserManager):
        def get_queryset(self):
            return super().get_queryset().filter(deleted_at__isnull=True)
    
    objects = UserManager()
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    
    LEVEL_CHOICES = [ 
                     ("L1", "Level 1"), 
                     ("L2", "Level 2"), 
                     ("L3", "Level 3"), 
                     ("M1", "Master 1"), 
                     ("M2", "Master 2"), 
                     ("PreDoc", "Pre Doctorate"), 
                     ("PhD", "PhD"), 
                     ("Pr", "Professor") 
                     ]
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return User(email, make_password(password), **extra_fields)
    
    def save(self, *args, **kwargs):
        if self.deleted_at is None:
            super().save(*args, **kwargs)
        else:pass
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    registration_number = models.CharField(unique=True, max_length=15)
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    profile_picture = models.FileField(null=True, blank=True)
    
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default="L1")
    school_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    bachelor_graduate_since = models.DateField(blank=True, null=True)
    master_graduate_since = models.DateField(blank=True, null=True)
    phd_graduate_since = models.DateField(blank=True, null=True)
    field_of_research = models.CharField(max_length=255, null=True)
    palmares = models.TextField(max_length=255, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    
    is_student = models.BooleanField(default=True)
    is_elder = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        
    def restore(self):
        self.deleted_at = None
        self.save()
        
    def update(self):
        self.updated_at = timezone.now()
        self.save()


    def set_password(self, password):
        self.password = password
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['*']
    
    is_authenticated = models.BooleanField(default=True)
    
    # def send_message(self, user, text, media):
    #     chat =  Chat()
    #     chat.save(f"{self.id}-{user.id}")
    #     mc = MessageContent.objects.create(text=text, attached_file=media)
    #     message = Message(self, user, chat, mc)
    #     message.save()
    #     return message

    # def reply_message(self, message, text, media):
    #     mc = MessageContent.objects.create(text=text, attached_file=media)
    #     reply = Message(message.receiver, message.sender, message.chat, mc)
    #     reply.save()
    #     return reply
        
    # def delete_message(self, message):
    #     if message.sender_id == self.id:
    #         message.delete()
    #         return True
    #     else:
    #         return False
    
    # def show_conversation(self, user):
    #     messages = Message.objects.filter(chat_id=f"{self.id}-{user.id}")
    #     return messages







class SubjectOfInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    




class SchoolElder(User):
    
    # def new_chat(self):
    #     chat = Chat.objects.get_or_create(created_by=self.id)
    #     chat.save()
    #     return JsonResponse({'success': True, 'message' : chat})
    def save(self, *args, **kwargs):
        self.is_student = False
        self.is_elder = True
        self.is_teacher = False
        super().save(*args, **kwargs)
    
    # def new_forum(self, name, purpose=None):
    #     chat =  Chat()
    #     chat.save(f"{self.id}-{timezone.now().strftime}")
    #     forum = Forum.objects.create(name=name, purpose=purpose, chat_id=chat.id, created_by=self.id)
    #     return forum
    
    def new_post():pass
    def comment_post():pass
    def like_post():pass
    def share_post():pass
    
class Teacher(User):
    
    # def new_chat(self):
    #     chat = Chat.objects.get_or_create(created_by=self.id)
    #     chat.save()
    #     return JsonResponse({'success': True, 'message' : chat})

    
    # def new_forum(self, name, purpose=None):
    #     chat =  Chat()
    #     chat.save(f"{self.id}-{timezone.now().strftime}")
    #     forum = Forum.objects.create(name=name, purpose=purpose, chat_id=chat.id, created_by=self.id)
    #     return forum
    
    def new_post():pass
    def comment_post():pass
    def like_post():pass
    def share_post():pass
    
    def save(self, *args, **kwargs):
        self.is_student = False
        self.is_elder = False
        self.is_teacher = True
        super().save(*args, **kwargs)
    


    # def get_participants(self):
    #     participants = []
    #     ids = ParticipantsForum.objects.filter(forum_id=self.id, user_id=self.id)
    #     if ids is not None:
    #         for id in ids:
    #             participants.append(User.objects.get(id=id))
    #     return participants
    
    # def add_participant(self, user):
    #     ParticipantsForum.object.create(forum_id=self.id, user_id=user.id)
    #     return True
    
    # def remove_participant(self, user):
    #     ParticipantsForum.object.get(forum_id=self.id, user_id=user.id).delete()
    #     return True
    
    # def number_of_participants(self):
    #     elements = ParticipantsForum.object.filter(forum_id=self.id)
    #     return len(elements)


    
