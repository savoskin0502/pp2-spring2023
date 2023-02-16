def chain(list1, list2):
    yield from list1
    yield from list2


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [4, 5, 6]

    c = chain(a, b)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
# for i in chain(a, b):
#     print(i)
