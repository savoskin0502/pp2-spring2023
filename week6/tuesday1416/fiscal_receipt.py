import re
from collections import namedtuple

import utils
text = utils.read_file(fpath='rawdata.txt')

pattern = r'ПРОДАЖА(?P<body>.*)Банковская карта'

matching_body = re.search(pattern, text, re.DOTALL)
fiscal_body = matching_body.group('body')

pattern_goods = r'(?P<number>\d+).*\n(?P<name>.*)\n(?P<count>.*) x (?P<price>.*)\n(.*)\nСтоимость\n(?P<totalPrice>.*)'
# matching_goods = re.search(pattern_goods, fiscal_body)
matching_goods = re.findall(pattern_goods, fiscal_body)

Good = namedtuple('Good', ['number', 'name', 'count', 'price', 'b', 'totalPrice'])

for good in matching_goods:
    g = Good(*good)
    print(g.name)
# print(matching_goods)
# if matching_goods is not None:
#     print(matching_goods.group('number'), matching_goods.groups())
# else:
#     print('looose')
