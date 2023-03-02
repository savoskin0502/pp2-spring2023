import shutil

shutil.copy('./rawdata.py', './tests/rawdata.py')
shutil.copy('./rawdata.py', './tests/rawdata-1.py')
# shutil.copytree('./abv', './tests/ab')
# shutil.move('./tests/a.txt', './tests/a1.txt')
shutil.move('./tests/a1.txt', './tests/ab/1.txt')

