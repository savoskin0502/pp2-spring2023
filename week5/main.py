import json


def producer(n):
    i = 0
    while i < n:
        yield i
        i += 1


def processing(sequence):
    for item in sequence:
        yield item + 5


def consumer(sequence):
    for item in sequence:
        # print('prepared, item', item)
        yield f"prepared item {item}"


# a = producer(n=5)
# b = processing(sequence=a)
# c = consumer(sequence=b)
# for element in c:
#     print(element)


class Human:
    def __init__(self):
        self.name = 'roma'


class HumanEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


obj = json.dumps(Human(), cls=HumanEncoder)
print(obj, type(obj))
