import re

text = ''  # cat, cot, ct, cit, cft
pattern = 'c[aoi]t'

matching = re.search(pattern, text)
if matching is not None:
    print(matching)
else:
    print('no match')
# pattern - something that we wan't to find
# text - where we will find
#

# acceptable_chars = ['a', 'o', 'i', 'f']
#
# for char in acceptable_chars:
#     cat_substr = 'c' + char + 't'
#     print(cat_substr in text)

# print(
#     'cat' in text
# )

