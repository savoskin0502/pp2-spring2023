import re

import utils
from utils import read_file
# data = utils.read_file(fpath='rawdata.txt')
text = '001002003004 БИН 001002003ab4 001002003004'

pattern = r'БИН.*?([0-9a-z]{12,12})' # .*
# (1 + ( 2 - 3 )) + (3 * 5 )
p = re.compile(pattern)
m = p.search(text)
print(m)
if m is not None:
    print(m.group(1), m.groups())
else:
    print('no match')

# print(text)

# \d - 0-9
# \s - пробелы
# \w - буквы; a-z
