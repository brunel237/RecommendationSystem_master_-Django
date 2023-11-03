from .factories import *
from django.db import IntegrityError

def seed_student(number):
    for _ in range(number):
        stu = StudentFactory.create_student()
        
def seed_school_elder(number):
    for _ in range(number):
        stu = SchoolElderFactory.create_school_elder()
            
def seed_lecturer(number):
    for _ in range(number):
        stu = LecturerFactory.create_lecturer()
                
def seed_courses(number):
    for _ in range(number):
        course = AcademicLevelCourseFactory()
    
def seed_all():
    # seed_courses(1)
    seed_student(29)
    seed_school_elder(10)
    seed_lecturer(25)