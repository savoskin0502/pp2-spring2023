class Human:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"Human(name={self.name}, city={self.city})"

    def __repr__(self):
        return self.__str__()


class Factory:
    def __init__(self, employees: list[Human]):
        self.employees = employees

    def __iter__(self):
        return self.employees.__iter__()

    def __len__(self):
        return len(self.employees)

    def __getitem__(self, i):  # item - index
        return self.employees[i]


# len()
# employees[5]


human1 = Human(name='aidana', city='astana')
human2 = Human(name='aibek', city='almaty')
factory = Factory(employees=[human1, human2])
print(factory.employees)
for employee in factory:  # for employee in factory:
    print(employee.name)

print(len(factory))
print(factory[-1])
