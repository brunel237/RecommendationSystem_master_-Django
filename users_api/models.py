from datetime import date
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db import transaction

from courses_api.models import *
# from inbox_api.models import Inbox


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
    # def create_user(self, username, email, password=None, **extra_fields):
    #     return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    STATUS_CHOICES = [('student', 'Student'), ('school_elder', 'School Elder'), ('lecturer', 'Lecturer')]

    date_of_birth = models.DateField(default=date.today)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    registration_number = models.CharField(unique=True, max_length=15)
    phone_number = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True, default="profile_default.png")

    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    last_login = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    
    def get_user(self):
        if self.status == "student":
            user = get_object_or_404(Student.objects.select_related('user'), user=self.id)
        elif self.status == "school_elder":
            user = get_object_or_404(SchoolElder.objects.select_related('user'), user=self.id)
        else:
            user = get_object_or_404(Lecturer.objects.select_related('user'), user=self.id)
        return user

    def follow(self, elder):
        if elder.status == "student":
            return False
        elder.followers.add(self)
        elder.number_followers += 1
        elder.save()
        return True

    def stop_follow(self, elder):
        elder.followers.remove(self)
        elder.number_followers -= 1
        elder.save()
        return True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def update(self):
        self.updated_at = timezone.now()
        self.save()


class Mentor(models.Model):
    school_elder = models.ForeignKey('SchoolElder', on_delete=models.SET_NULL, null=True, blank=True)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    courses_attending = models.ManyToManyField(AcademicLevelCourse, related_name='student_courses')
    academic_mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL,related_name='academic_mentor', blank=True, null=True)
    
    def get_student(self):
        student = Student.objects.select_related('user').get(id=self.id)
        return student
    
    def set_mentor(self, mentor):
        if mentor.status == "school_elder":
            mentor, _ = Mentor.objects.get_or_create(school_elder=mentor)
        else: 
            mentor, _ = Mentor.objects.get_or_create(lecturer=mentor)
        self.academic_mentor = mentor
        self.save()
        return True

    def get_mentor(self):
        mentor = Mentor.objects.get(student=self)
        if mentor is not None:
            if mentor.school_elder is not None:
                return SchoolElder.objects.select_related('user').get(mentor.school_elder)
            else:
                return Lecturer.objects.select_related('user').get(mentor.lecturer)
        return False
    
    def mentor_reset(self, mentor):
        mentor = Mentor.objects.get(mentor)
        if mentor.student == self:
            self.academic_mentor = None
            self.save()
            return True
        return False


class SchoolElder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='school_elder')
    courses_attending = models.ManyToManyField(AcademicLevelCourse, related_name='school_elders_courses')
    notoriety = models.IntegerField(default=0)
    followers = models.ManyToManyField(User, related_name='school_elder_followers')
    number_followers = models.IntegerField(default=0)

    bachelor_graduate_since = models.DateField()
    master_graduate_since = models.DateField(blank=True, null=True)
    is_mentor = models.BooleanField(default=False)
    
    def get_school_elder(self):
        elder = SchoolElder.objects.select_related('user').get(id=self.id)
        return elder

    def mentoring(self, student):
        try:
            with transaction.atomic():
                if student.set_mentor(self):
                    self.is_mentor = True
                    self.mentoring_number += 1
                    self.save()
                    return True
        except:
            return False
        
    def stop_mentoring(self, student):
        try:
            with transaction.atomic():
                if student.mentor_reset(self):
                    self.mentoring_number -= 1
                    if self.mentoring_number == 0:
                        self.is_mentor = False
                    self.save()
                    return True
        except:
            return False


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer')
    lectures = models.ManyToManyField(AcademicLevelCourse, related_name='lectures')
    notoriety = models.IntegerField(default=0)
    is_mentor = models.BooleanField(default=False)
    mentoring_number = models.IntegerField(default=0)
    followers = models.ManyToManyField(User, related_name='lecturer_followers')
    number_followers = models.IntegerField(default=0)

    TITLES = [('phd', 'PhD'), ('pr', 'Professor')]
    title = models.CharField(max_length=5, choices=TITLES)

    bachelor_graduate_since = models.DateField()
    master_graduate_since = models.DateField()
    phd_graduate_since = models.DateField()
    field_of_research = models.CharField(max_length=255, default="None")
    biography = models.TextField(default="None")
    
    def get_lecturer(self):
        lecturer = Lecturer.objects.select_related('user').get(id=self.id)
        return lecturer

    def mentoring(self, student):
        try:
            with transaction.atomic():
                if student.set_mentor(self):
                    self.is_mentor = True
                    self.mentoring_number += 1
                    self.save()
                    return True
        except:
            return False
        
    def stop_mentoring(self, student):
        try:
            with transaction.atomic():
                if student.mentor_reset(self):
                    self.mentoring_number -= 1
                    if self.mentoring_number == 0:
                        self.is_mentor = False
                    self.save()
                    return True
        except:
            return False
        

# user = User.objects.get(id=80)
# print(type(user))

# users = User.objects.prefetch_related('student').all()
# student = Student.objects.select_related('user').get(id=1)
# students = Student.objects.select_related('user').all()