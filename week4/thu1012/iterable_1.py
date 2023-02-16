class FirstNumbers:
    def __init__(self, n):
        self.last_number = n
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < self.last_number:
            self.current_number += 1
            return self.current_number - 1
        raise StopIteration
# list -> __iter__(); __next__(); raise StopIteration
# 1 + 2

# for i in FirstNumbers(n=5):  # __next__() - 1; __next__() - 2
#     print(i)


a = FirstNumbers(n=5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
