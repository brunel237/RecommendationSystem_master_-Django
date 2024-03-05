import random
import factory
# import models
from factory.django import DjangoModelFactory
from faker import Faker
from factory.fuzzy import FuzzyText
from .models import *


fake = Faker()

class FacultyFactory(DjangoModelFactory):
    class Meta:
        model = Faculty

    faculty_of = fake.unique.job()
    dean = fake.unique.name()
    # faculty_of = factory.Faker("job")
    # dean = factory.Faker("name")


class AcademicLevelFactory(DjangoModelFactory):
    class Meta:
        model = AcademicLevel

    level = factory.Iterator([choice[0] for choice in AcademicLevel.LEVEL_CHOICES])


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    # department_of = factory.Faker("job")
    # hod = factory.Faker("name")
    department_of = fake.unique.job()
    hod = fake.unique.name()
    # faculty = factory.SubFactory(FacultyFactory)
    # faculty = Faculty.objects.get(id= random.randint(6, 12 ))
    faculty = FacultyFactory()
    

class CourseOfStudyFactory(DjangoModelFactory):
    class Meta:
        model = CourseOfStudy

    course_code = fake.random_number(digits=4)
    course_name = fake.job()
    is_research_field = fake.boolean()
    description = fake.text()


class AcademicLevelCourseFactory(DjangoModelFactory):
    class Meta:
        model = AcademicLevelCourse

    course = CourseOfStudyFactory()
    level = AcademicLevelFactory()
    department = DepartmentFactory()
    # level = AcademicLevel.objects.get(id= random.randint(1, 6))
    # department = Department.objects.get(id= random.randint(11, 43 ))
    # course = CourseOfStudy.objects.get(id= random.randint(2, 101))


def seed_database(num=3):
    for _ in range(num):
        AcademicLevelCourseFactory()


if __name__ == '__main__':
    seed_database()

