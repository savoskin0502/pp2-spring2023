class FirstN:
    def __init__(self, n):
        self.current = 0
        self.end_number = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end_number:
            self.current += 1
            return self.current - 1
        raise StopIteration


first = FirstN(n=5)  # __iter__
for i in first:  # __next__()
    print(i)
