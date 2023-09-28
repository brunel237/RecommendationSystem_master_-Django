from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password


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
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return User(email, make_password(password), **extra_fields)
    
    def save(self, *args, **kwargs):
        if self.deleted_at is None:
            super().save(*args, **kwargs)
        else:
            pass
    
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
    
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    deleted_at = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    # is_superuser = models.BooleanField(default=False)
    
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
    # @property
    # def is_authenticated(self):
    #     return True if self.is_active else False

