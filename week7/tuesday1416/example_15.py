
class CustomException(Exception):
    pass

# f = open('./rawdata.txt')
try:
    number = 5
    div = input()
    if not div.isdigit():
        raise CustomException

except (ValueError, ZeroDivisionError) as err:
    print(type(err))
    print('без комментариев')
except ImportError:
    print('a')
except Exception as err:
    print('log', err)
    raise err
else:
    print('без ошибок')
finally:
    print('finally block')
    # f.close()
