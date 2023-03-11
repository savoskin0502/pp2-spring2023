

class Human:
    # slots
    def __init__(self, name):
        self.name = name

    def test(self):
        pass


human = Human(name='roma')
print(human.__dict__)
human.age = 23
print(human.__dict__)
human.__dict__['city'] = 'Almaty'
print(human.__dict__)
# print(dict(human))
