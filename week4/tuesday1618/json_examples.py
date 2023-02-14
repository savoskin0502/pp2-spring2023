import json


class Human:
    def __init__(self, name):
        self.name = name


class HumanSerializer(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
        # return {
        #     'name': o.name
        # }


human = {
    "name": 'roma',
    "city": "almaty"
}


thuman = """{
    "name": 'roma',
    "city": "almaty"
}"""
# f = open('/Users/roman/Desktop/pp2-spring2023/plan.md')
# dictionary = json.loads(f.read())

# json.loads(thuman)
text_human = json.dumps(human)
obj = Human(name='roma')

print(type(human), type(text_human))
print(human)
print(text_human)
print(json.dumps(obj, cls=HumanSerializer))  # => json.dumps({'name': 'roma})
