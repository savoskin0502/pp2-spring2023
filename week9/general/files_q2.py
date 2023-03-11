import collections
import os
import shutil

path = os.getcwd()
new_path = os.path.join(path, 'newFolder')

# results = {}
results = collections.defaultdict(int)
delta = 1


if not os.path.exists(new_path):
    os.makedirs(new_path)


# os.listdir -
for file in os.listdir(path):
    fpath = os.path.join(path, file)
    if os.path.isdir(fpath):
        continue

    extension = file.split('.')[-1]
    results[extension] += delta

    if extension == 'txt':
        new_fpath = os.path.join(new_path, file)  #  new_path + file
        shutil.move(fpath, new_fpath)
        # os.remove(fpath)


for extension, count in results.items():
    print(extension, '-', count)
# print(results)
