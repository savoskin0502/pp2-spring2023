import re

import utils

text = utils.read_file('rawdata.txt')
pattern = r'филиал *(?P<filial>.*)\nБИН.*?(?P<bin>\d{12,12})\nНДС(?P<nds>.*?)'
# \w; \s; \number
p = re.compile(pattern)
matching = p.search(text)

# matching = re.search(pattern, text)  # re.match()
# re.compile() #
# pattern - 1. prepare/compile 2. use pattern


if matching is not None:  # ==; !=
    print('Match found: ', matching.group())
else:
    print('No match')
# print(matching)
# print(matching.groups())  # None.groups()
# print(matching.group('filial'))  # or print(matching.group(1))
