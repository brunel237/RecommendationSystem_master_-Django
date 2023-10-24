from django.db import models
from django.db import transaction
from abc import ABC, abstractmethod

class Privilege:
    @abstractmethod 
    def mentoring(self, student):
        pass
    
    def remove_follower(self, follower):
        self.followers.remove(follower)
        self.number_followers -= 1
        self.save()
    
    def stop_mentoring(self, student):
        try:
            with transaction.atomic():
                if student.mentor_id == self.id:
                    student.mentor_id = None
                    student.mentor_type = None
                    student.academic_mentor = None
                    student.save()
                    self.mentoring_number -= 1
                    if self.mentoring_number == 0:
                        self.is_mentor = False
                    self.save()
                    return True
                return False
        except:
            return False

    