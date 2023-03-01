import os

fpath = 'rawdata.txt'
# print(fpath)
print(
    os.path.join(
        os.getcwd(),
        'tests',
        fpath,
    )
)
os.remove('raw')
# print(os.path.abspath(fpath))
if os.path.exists(fpath):
    os.remove(fpath)
    print('del file')
