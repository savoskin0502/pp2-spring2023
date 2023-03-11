import os.path
import re


def extract_even_lines(fpath):
    for line_number, line in enumerate(read_file(fpath), 1):
        if line_number % 2 == 0:
            yield delete_digits(line)


def delete_digits(text, pattern=r'\d'):
    return re.sub(pattern, '', text).strip()


def read_file(fpath):
    with open(fpath, mode='r') as file:
        for line in file:
            yield line


path = os.path.join(os.getcwd(), 'data.txt')
f = extract_even_lines(path)
print(next(f))
print(next(f))
