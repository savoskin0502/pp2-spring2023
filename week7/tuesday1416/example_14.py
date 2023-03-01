
try:
    number = 5
    div = int(input())
    print(number / div)
except ZeroDivisionError as err:
    print('да и пофиг', err)
