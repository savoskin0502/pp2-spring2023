def chain(list1, list2):
    yield from list1  # 1, 2, 3
    yield from list2  # 4, 5, 6


l1 = [1, 2, 3]
l2 = [4, 5, 6]

for item in chain(l1, l2):
    print(item)  # => 1, 2, 3, 4, 5, 6
