
class Factory:
    def __init__(self, employees: list):
        self.employees = employees

    def __getitem__(self, idx):  # чтобы обращаться по индексам
        return self.employees[idx]

    def __len__(self):  # чтобы длину получить
        return len(self.employees)


class Human:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"Human(name={self.name})"


empl = [Human(name='aibek', city='almaty'), Human(name='aida', city='astana')]
factory = Factory(employees=empl)
print(
    factory[0],  # factory.employees[0]
    len(factory),
)
