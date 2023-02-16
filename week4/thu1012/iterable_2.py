# range_example = range(1, 1_000_000_000_000)
# print(range_example)

# list_example = [i for i in range(1, 1_000_000_000_000)]
# list_example = [0] * 1_000_000_000_000
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def count(n):
    # __iter_()_; __next__()
    print('hello, from count')
    idx = 0
    # l = []
    while idx < n:
        yield idx
        idx += 1
        # l.append(idx)
    # return l


def display():
    print('hello, world')


counter_obj = count(n=5)
print(next(counter_obj))
print(next(counter_obj))
print(next(counter_obj))
print(next(counter_obj))
print(next(counter_obj))
# print(next(counter_obj))
print(display())
