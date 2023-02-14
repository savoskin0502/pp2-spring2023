# range_examples - module

# range_number = range(0, 1_000_000_000)  # work only with 1 element
# print(range_number)
# numbers_list = [i for i in range(0, 1_000_000_000)] # we try to append 1bil elements into our list



def range_analog(n):
    current_number = 0
    while current_number < n:
        # return current_number
        yield current_number
        current_number += 1


numbers = range_analog(5) # __iter__()
for number in numbers:  # __next__()
    print(number)
print(type(numbers))
