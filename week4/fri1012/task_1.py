import datetime
import collections

Group = collections.namedtuple('Group', ['low', 'upper', 'name'])


class User:
    groups = (
        Group(0, 12, 'Child'),
        Group(13, 17, 'Adolescent'),
        Group(18, 65, 'Adult'),
        Group(65, 1_000, 'Old Adult')
    )

    def __init__(self, username, age, gender, created_at: datetime.datetime = None):
        self.username = username
        self.age = age
        self.gender = gender
        self.created_at = self.setup_created_at(created_at=created_at)

    @staticmethod
    def setup_created_at(created_at):
        if created_at is None:
            return datetime.datetime.now()
        return created_at

    @property
    def group(self):
        # Group(low, upper, group)

        # for low, upper, group in self.groups:
        #     if low <= self.age <= upper:
        #         return group

        for group in self.groups:
            if group.low <= self.age <= group.upper:
                return group.name

        print('твой возраст выглядит странным')

    def __str__(self):
        return f"User(username={self.username})"


def fake_user_generator():
    for _ in range(100):
        data = {
            'username': '1',
            'age': 18,
            'gender': 'mf',
        }
        yield data


user = User(username='sv-roman', age=23, gender='m')
print(user.group)
print(user.__dict__)

user_creator = fake_user_generator()
user1 = User(**next(user_creator))
print(user1)
