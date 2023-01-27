numbers = [(1, 2, 5), (2, 3), (3, 7), (4, 16)]

for idx, values in enumerate(numbers):
    tmp = 1
    for value in values:
        tmp *= value

    numbers[idx] = tmp

print(numbers)
