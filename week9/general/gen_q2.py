def even_numbers(n):
    number = 2

    while True:
        yield number ** n
        number += 2
