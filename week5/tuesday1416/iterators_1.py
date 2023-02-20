class Factory:
    def __init__(self, employees):
        self.employees = employees

    def __iter__(self):
        return self.employees.__iter__()

    # def __next__(self):
        # list - __iter__() => __next__()
        # raise StopIteration
    def __len__(self):
        return len(self.employees)

    def __getitem__(self, item):
        return self.employees[item]

    def __contains__(self, item):
        pass


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Human(name={self.name})"

    def __repr__(self):
        return self.__str__()


factory = Factory(employees=[Human(name='aidana'), Human(name='alibek')])
# print(factory.employees[0])
for employee in factory:
    print(employee)


print(len(factory))
print(factory[-1])
print('ok' in factory)


# simple_list = [1, 2, 3, 4, 5]  # for i in simple_list =>__next__() - 1; __next__() - 2 => raise StopIteration
