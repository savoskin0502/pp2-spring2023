def chain(numbers1: list, numbers2: list):
    yield from numbers1
    yield from numbers2

    # for number in numbers1:
    #     yield number
    #
    # for number in numbers2:
    #     yield number


l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]

for item in chain(l1, l2):
    print(item)
