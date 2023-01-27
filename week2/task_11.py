number = int(input())

row_results = []
for idx in range(1, number, 10):
    for value in range(idx, idx + 10):
        if value % 5 == 0 and value % 3 == 0:
            row_results.append('FizzBuzz')
        elif value % 5 == 0:
            row_results.append('Buzz')
        elif value % 3 == 0:
            row_results.append('Fizz')
        else:
            row_results.append(str(value))

    print(',   '.join([f"{val:>8}" for val in row_results]))
    row_results.clear()
