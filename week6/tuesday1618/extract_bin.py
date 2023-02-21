import re

text = '001002233004 БИН 001002003004 001002343004 fasfasfasfafs'
pattern = 'БИН.*?(?P<bin>[0-9]{12,12}).*?([a-z]+)'  # ( 1 + (2 * 5 )) + (3 - 4)

matching = re.search(pattern, text)

# dictionary = {
#     'key': 'value'
# }

print(matching.group())
# print(matching.group())
# print(matching.group('bin'))
