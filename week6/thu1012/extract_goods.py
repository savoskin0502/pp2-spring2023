import collections
import re

import utils


Good = collections.namedtuple('Good', ['id', 'name', 'count', 'price_item'])


def extract_body(text):
    pattern = r'продажа(.*)банковская\s*?карта'
    matching = re.search(pattern=pattern, string=text, flags=re.DOTALL | re.IGNORECASE)
    goods_text = matching.group()
    return goods_text


def extract_goods(text):
    pattern = r'(?P<id>(\d+).*\n(?P<name>.*)\n(?P<count>.*?)\s*?x\s*?(?P<pricePerItem>.*)\n'
    matching = re.finditer(pattern, text)

    for item in matching:  # __iter__(); __next__()
        yield Good(*item.groups())
    # print(matching.group())
    # print(matching.group('count'), matching.group('pricePerItem'))


if __name__ == '__main__':
    content = utils.read_file('rawdata.txt')
    body = extract_body(text=content)
    goods = extract_goods(text=body)
    good = next(goods)
    print(
        good.id,
        good.name,
        good.price_item,
        good.count,
    )
