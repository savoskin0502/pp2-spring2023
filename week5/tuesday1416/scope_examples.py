x = 10  # global

# int = str # don't do that


def increment():  # local
    global x
    x += 1  # nonlocal -> local -> global -> builtin ( str, print, input )


passengers = []


def add_passenger():
    passengers.append(1)


add_passenger()
print(passengers)
