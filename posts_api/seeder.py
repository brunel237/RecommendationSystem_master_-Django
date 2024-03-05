import random
import factory
# import models
from factory.django import DjangoModelFactory
from faker import Faker
from factory.fuzzy import FuzzyText
from .models import *


fake = Faker()


class PostFactory(DjangoModelFactory):

    class Meta:
        model = Post
    
    @staticmethod
    def create_post():
        post_data = {
            'author': User.objects.get(id=random.randint(378, 770)),
            'message': fake.sentence(nb_words=random.randint(5, 50)),
        }

        post = Post.objects.create(**post_data)
        return post
    @staticmethod

    def post_like():
        author  =  User.objects.get(id=random.randint(378, 770))
        post  =  Post.objects.get(id=random.randint(46, 196))

        like = Like.like_post(author=author, post=post)

        return like


def seed_database(num=5):
    for _ in range(num):
        # PostFactory.create_post()
        PostFactory.post_like()




