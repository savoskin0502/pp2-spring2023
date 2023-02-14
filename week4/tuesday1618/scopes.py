counter = 0


def increment():  # local -> global -> built-in - print/input/int, set(),
    global counter
    counter += 1


passengers = []
# tuples - immutable; str - imm; int/float - immutable; arrays
# lists, set, dicts


def add_passenger():
    passengers.append(1)


# increment()
# print(counter)
add_passenger()
add_passenger()

print(passengers)
