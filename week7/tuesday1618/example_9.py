import os

fpath = 'rawdata.txt'
print(os.path.abspath(fpath))


print(
    os.path.join(
        os.getcwd(),
        'tests',
        'a.txt'
    )
)
