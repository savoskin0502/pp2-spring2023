import collections
import datetime
import random
# faker

Group = collections.namedtuple('Group', ['lower', 'upper', 'name'])


class User(object):
    groups = (
        Group(0, 12, 'Child'),
        Group(13, 17, 'Adolescent'),
        Group(18, 65, 'Adult'),
        Group(66, 1_000, 'Old adult'),
    )

    def __init__(self, username, age, gender, created_at=None):
        self.username = username
        self.age = age
        self.gender = gender  # male/female
        self.created_at = created_at

    def __new__(cls, username, age, gender, **kwargs):
        if gender not in {'female', 'male'}:
            raise ValueError('что ты такое')

        if not (0 <= age <= 100):
            raise ValueError('фейс контроль не проходишь')

        return super().__new__(cls)

    @property
    def group(self):
        for group in self.groups:
            if group.lower <= self.age <= group.upper:
                return group.name

    def __str__(self):
        return f"User(username={self.username}, sex={self.gender}, created_at={self.created_at})"


def user_factory():
    for _ in range(100):
        data = {
            'username': ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(5, 12))]),
            "age": random.randint(0, 100),
            'gender': random.choice(['male', 'female']),
        }
        yield User(**data)


user = User(username='sv-roman', age=23, gender='male')
factory = user_factory()
print(next(factory))
print(user.group)  # user.group
