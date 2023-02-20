def chain(list1, list2):
    yield from list1
    yield from list2


l1 = [1, 2, 3]
l2 = [4, 5, 6]
for i in chain(l1, l2):
    print(i)
