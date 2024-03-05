import random
import factory
# import models
from factory.django import DjangoModelFactory
from faker import Faker
from django.contrib.auth.hashers import make_password
from factory.fuzzy import FuzzyText
from .models import *


fake = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


    @staticmethod
    def create_user(status):
        user_data = {
            'username': fake.unique.user_name(),
            'password': make_password("123456"),
            'date_of_birth': fake.date_of_birth(),
            'sex': fake.random_element(elements=('male', 'female')),
            'registration_number' : fake.random_number(digits=10),
            'first_name' : fake.first_name(),
            'last_name' : fake.last_name(),
            'phone_number' : fake.unique.phone_number(),
            'address' : fake.address(),
            'email' : fake.unique.safe_email(),
            'status': status,
        }

        user = User.objects.create(**user_data)
        return user


class StudentFactory:
    @staticmethod
    def create_student():
        user = UserFactory.create_user("student")
        # courses_attending = CourseOfStudy.objects.order_by('?')[:random.randint(1, 5)]
        student = Student.objects.create(user=user)
        # student.courses_attending.set(courses_attending)
        return student


class SchoolElderFactory:
    @staticmethod
    def create_school_elder():
        user = UserFactory.create_user("school_elder")
        school_elder_data = {
            'bachelor_graduate_since': fake.date(),
            'master_graduate_since': fake.date(),
        }
        # courses_attending = CourseOfStudy.objects.order_by('?')[:random.randint(1, 5)]
        school_elder = SchoolElder.objects.create(user=user, **school_elder_data)
        # school_elder.courses_attending.set(courses_attending)
        return school_elder


class LecturerFactory:
    @staticmethod
    def create_lecturer():
        user = UserFactory.create_user("lecturer")
        lecturer_data = {
            'bachelor_graduate_since': fake.date(),
            'master_graduate_since': fake.date(),
            'phd_graduate_since': fake.date(),
            'field_of_research': fake.job(),
            'biography': fake.text(),
            'title': fake.random_element(elements=('PhD', 'Pr'))
        }
        # lectures = CourseOfStudy.objects.order_by('?')[:random.randint(1, 5)]
        lecturer = Lecturer.objects.create(user=user, **lecturer_data)
        # lecturer.lectures.set(lectures)
        return lecturer


def seed_database(num=5):
    for _ in range(num):
        StudentFactory.create_student()
        SchoolElderFactory.create_school_elder()
        LecturerFactory.create_lecturer()


