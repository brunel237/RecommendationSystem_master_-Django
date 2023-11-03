import random
from faker import Factory, Faker
import factory
# from users_api.models import *

user = User.objects.get(id=80)
print(type(user))

fake = Faker()

# print(dir(fake))

# random_number =   factory.LazyAttribute(lambda x: random.randrange(0, 10000))

# print(random_number)
