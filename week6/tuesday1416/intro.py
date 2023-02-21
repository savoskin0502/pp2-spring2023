import re

text = 'abcabcfgh'  # \\d - 0-9; \s; \w
pattern = 'abc'
print('\\\\fdfs')

matching = re.search(pattern, text)
matching_match = re.match(pattern, text)
print(matching_match)
if matching:
    print('Match found: ', matching.group()) # groups()
else:
    print('No match')

# pattern - то что я ищу
# text - в котором буду искать
# правила извлечения