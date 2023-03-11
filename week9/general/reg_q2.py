import re

text = "hello my abbd hey hey ab"
pattern = r'[aA][bB]'  # ab => bc; \b \d{3,3}

text = re.sub(pattern, 'bc', text)

with open('data.txt', mode='w', encoding='utf8') as f:
    f.write(text)
