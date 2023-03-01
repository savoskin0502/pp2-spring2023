import re

text = '121122123124 БИН адлыр 312443  аывордаыдвлоа 001002003004 алывралыдоа 001342003344 аыдвлраыдвоал'
pattern = 'БИН.*?(\d{12,12})'  # . - any symbol ( 0-9, _, abcdef )
# \w; \d; \s
# ( ( 1 + 2 ) * 4) + 5
print(re.search(pattern, text).group(0))
print(re.search(pattern, text).group(1))
