import os

fpath = './tests/t1/t2/t3/t33'

if not os.path.exists(fpath):
    # os.mkdir(fpath)
    os.makedirs(fpath)

os.rmdir('./tests/t1')

# to_delete = ['a.txt', 'b.txt']
# for file in to_delete:
#     os.rmdir(file)
