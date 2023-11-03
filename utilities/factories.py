import random
import factory
from factory.django import DjangoModelFactory
from faker import Faker
from django.contrib.auth.hashers import make_password

from courses_api.models import *
from faculties_api.models import *
from departments_api.models import *
from users_api.models import *

fake = Faker()


class FacultyFactory(DjangoModelFactory):
    class Meta:
        model = Faculty

    faculty_of = factory.Faker("job")
    dean = factory.Faker("name")


class AcademicLevelFactory(DjangoModelFactory):
    class Meta:
        model = AcademicLevel

    level = factory.Iterator([choice[0] for choice in AcademicLevel.LEVEL_CHOICES])


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    department_of = factory.Faker("job")
    hod = factory.Faker("name")
    # faculty = factory.SubFactory(FacultyFactory)
    faculty = Faculty.objects.get(id= random.randint(6, 12 ))
    

class CourseOfStudyFactory(DjangoModelFactory):
    class Meta:
        model = CourseOfStudy

    course_code = factory.Faker("sentence", nb_words=1)
    course_name = factory.Faker("sentence", nb_words=3)
    is_research_field = factory.Faker("boolean")
    description = factory.Faker("text", max_nb_chars=100)


class AcademicLevelCourseFactory(DjangoModelFactory):
    class Meta:
        model = AcademicLevelCourse

    level = AcademicLevel.objects.get(id= random.randint(1, 6))
    department = Department.objects.get(id= random.randint(11, 43 ))
    course = CourseOfStudy.objects.get(id= random.randint(2, 101))



class UserFactory:
    @staticmethod
    def create_user():
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
            'status':"lecturer",
        }
        
        user = User.objects.create(**user_data)
        return user


class StudentFactory:
    @staticmethod
    def create_student():
        user = UserFactory.create_user()
        courses_attending = CourseOfStudy.objects.order_by('?')[:random.randint(1, 5)]
        student = Student.objects.create(user=user)
        student.courses_attending.set(courses_attending)
        return student


class SchoolElderFactory:
    @staticmethod
    def create_school_elder():
        user = UserFactory.create_user()
        school_elder_data = {
            'bachelor_graduate_since': fake.date(),
            'master_graduate_since': fake.date(),
        }
        courses_attending = CourseOfStudy.objects.order_by('?')[:random.randint(1, 5)]
        school_elder = SchoolElder.objects.create(user=user, **school_elder_data)
        school_elder.courses_attending.set(courses_attending)
        return school_elder


class LecturerFactory:
    @staticmethod
    def create_lecturer():
        user = UserFactory.create_user()
        lecturer_data = {
            'bachelor_graduate_since': fake.date(),
            'master_graduate_since': fake.date(),
            'phd_graduate_since': fake.date(),
            'field_of_research': fake.job(),
            'biography': fake.text(),
            'title': fake.random_element(elements=('PhD', 'Pr'))
        }
        lectures = CourseOfStudy.objects.order_by('?')[:random.randint(1, 5)]
        lecturer = Lecturer.objects.create(user=user, **lecturer_data)
        lecturer.lectures.set(lectures)
        return lecturer


# class CourseOfStudyFactory:
#     @staticmethod
#     def create_course_of_study():
#         name = fake.unique.job()
#         code = fake.unique.random_number(digits=4)
#         course = CourseOfStudy.objects.create(name=name, code=code)
#         return course