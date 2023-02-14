import json

human = {
    "name": "roma",
    "city": "almaty"
}
text_human = """{
    "name": "roma",
    "city": "almaty"
}"""

json_human = json.dumps(human)
print(type(human), type(json_human))
print(human)
print(json_human)
dict_py_human = json.loads(text_human)
print(dict_py_human, type(dict_py_human))


class Human:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class HumanSerializer(json.JSONEncoder):
    def default(self, o):
        print(o.__dict__, 'dict')
        return o.__dict__
        # return {
        #     'name': o.name,
        #     'city': o.city,
        # }


human1 = Human(name='roma', city='almaty')
print(json.dumps(human1, cls=HumanSerializer))
# dict -> json
# object -> dict
f = open('fname')
dictionary = json.loads(f.read())
