list_examples = [1, 2, 3, 4, 5]  # raise StopIteration
set_examples = {1, 2, 3, 4}


for item in list_examples:  # __iter__(), __next__()
    print(item * 2)
