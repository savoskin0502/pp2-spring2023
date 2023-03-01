
class SimpleCustomError(Exception):
    pass


try:
    number = 5
    div = input()  # 5 / div

    if not div.isdigit():
        text = 'd' if True else 'a'
        raise IndexError(text)
    raise SimpleCustomError()
    # print(number / div)

except (ZeroDivisionError, ValueError) as err:
    print(type(err), err)
    print('are you cat?')
except ImportError:
    print('are you dog?')
else:
    print('else block')
finally:
    print('finally block')