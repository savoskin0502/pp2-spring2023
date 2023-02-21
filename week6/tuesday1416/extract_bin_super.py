import re

import utils
text = utils.read_file(fpath='rawdata.txt')
pattern_bin = r'БИН.*?(?P<BIN>[0-9a-z]{12,12})'
pattern_filial = r'(Филиал)\s(?P<Filial>.*)'
# ?P<BIN>
matching_bin = re.search(pattern_bin, text)
matching_filial = re.search(pattern_filial, text)
if matching_bin is not None:
    print(matching_bin.group('BIN'))

if matching_filial is not None:
    print(matching_filial.group('Filial'))
