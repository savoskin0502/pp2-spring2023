class RangeAnalog:
    def __init__(self, n):
        self.end_number = n
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < self.end_number:
            self.current_number += 1
            return self.current_number - 1
        raise StopIteration()


# simple_range = RangeAnalog(n=5)
for i in RangeAnalog(n=3):
    print(i)
