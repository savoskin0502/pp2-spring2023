import re

text = 'fsdufhsjdf fsdfjhsf \station'  # cat or cot
# pattern = 'c[ao]t'
pattern = r'^\\station$'  # \d - digit, from 0 to 9
# $; ^
print(text, pattern)

matching = re.search(pattern, text)
if matching:
    print('Match found: ', matching.group())  # groups()
else:
    print('No match')

