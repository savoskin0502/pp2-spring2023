
exceptions = (ValueError, ZeroDivisionError)


class UserNotFound(Exception):
    pass


try:
    number = 5
    div = input()

    if not div.isdigit():
        raise ValueError('bad number')
    div = int(div)
    print(number / div)
    # x = int("not an integer")
except exceptions as err:
    print("Invalid input", err, type(err))
except ImportError:
    print('imp error')
except UserNotFound as a:
    print('user not found', a)
else:
    print('ok')
finally:
    print('finally block')
