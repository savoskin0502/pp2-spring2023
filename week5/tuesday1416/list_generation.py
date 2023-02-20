def simple_generator(n):
    idx = 0
    while idx < n:
        yield idx
        idx += 1


if __name__ == '__main__':
    s = simple_generator(n=1_000_000_000)  # s - generator; next(s)
    print(s, 'hi from `list_generation`')
# for i in simple_generator(n=5):
#     print(i)
#
# s = simple_generator(5) # 0; gen -
# next(s)  # 0
# print(next(s))  # 1
# print(next(s)) # 2
# print(next(s)) # 3


# range_numbers = range(0, 1_000_000_000)


# list_numbers = [i for i in range(0, 1_0)]
# print(type(range_numbers), type(list_numbers))
