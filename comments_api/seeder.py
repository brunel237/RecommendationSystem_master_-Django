import random
import factory
# import models
from factory.django import DjangoModelFactory
from faker import Faker
from factory.fuzzy import FuzzyText
from .models import *



fake = Faker()


class CommentFactory(DjangoModelFactory):

    class Meta:
        model = Comment
    
    @staticmethod
    
    def comment_make():
        author  =  User.objects.get(id=random.randint(378, 770))
        post  =  Post.objects.get(id=random.randint(46, 196))
        content = fake.sentence(nb_words=random.randint(5, 20))

        cmt = Comment.make_comment(author=author, post=post, content=content)

        return cmt



def seed_database(num=5):
    for _ in range(num):
        # PostFactory.create_post()
        CommentFactory.comment_make()




