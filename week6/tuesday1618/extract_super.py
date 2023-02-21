import re

import utils


text = utils.read_file('rawdata.txt')
# pattern_bin = 'БИН (?P<bin>[0-9]{12,12})'
# matching_bin = re.search(pattern_bin, text)


# if matching_bin is not None:
#     print(matching_bin.group('bin'))
#
# pattern_filial = 'ФИЛИАЛ (?P<filial>.*)'
# matching_filial = re.search(pattern_filial, text, re.IGNORECASE)
#

# if matching_filial is not None:
#     print(matching_filial.group('filial'))

pattern_body = r'ПРОДАЖА(.*)Банковская карта'
matching_body = re.search(pattern_body, text, re.DOTALL)
goods = matching_body.group()

pattern_goods = r'(\d+).*\n(?P<name>.*)\n(.*) x (.*)\n'
matching_goods = re.findall(pattern_goods, goods)
print(matching_goods)
import collections
Good = collections.namedtuple('Good', ['id', 'name', 'count', 'pricePerItem'])

for good in matching_goods:
    g = Good(*good)
    print(g)


text = '<div><p>hello fd</p></div>'
pattern = r'>.*?<'
matching = re.search(pattern, text)
print(matching.group())
