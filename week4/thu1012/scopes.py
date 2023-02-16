# global
x = 5
passengers = []


def increment(x):  # local
    x = x + 1
    return x


def add_passengers():  # passengers
    global x
    x += 1
    # passengers = [2, 3]
    passengers.append(1)


# input = print # built-in
# input(1, 2, 3)
x = increment(x)
x = increment(x)
print(x)
# add_passengers()
# add_passengers()
# print(passengers)
# print(x)
