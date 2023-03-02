import os

fpath = './abv'

if not os.path.exists(fpath):
    os.mkdir(fpath)


fpath_nested = './abv/t1/t2/t3/t4'
if not os.path.exists(fpath):
    os.makedirs(fpath_nested)


if os.path.exists('rawdata.h'):
    os.remove('rawdata.h')


print(os.path.abspath('./abv'))
print(
    os.path.join(
        os.getcwd(),
        'tests',
        'b.txt',
    )
)
