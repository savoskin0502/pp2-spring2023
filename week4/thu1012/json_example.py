import json


human_example = {
    'name': 'roma',
    'city': 'almaty'
}

print(type(human_example), human_example)
human_json = json.dumps(human_example)
human_bytes = human_json.encode()

human_str = """{
    "name": "roma",
    "city": "almaty"
}"""

print(json.loads(human_str))
# human_bytes.decode() - str; -> json.loads(str) - dict


class Human:
    def __init__(self, name):
        self.name = name

    # def dict(self):
        # return {
        #     'name': self.name,
        #     'customField': 1
        # }


class A:
    pass


class ClassSerializer(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


human = Human(name='roma')
# print(json.dumps(human.dict()))
# print(json.dumps(human.__dict__))
print(json.dumps(human, cls=ClassSerializer))

