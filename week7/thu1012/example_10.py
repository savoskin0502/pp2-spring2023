import os

root_dir = "."
for dirpath, dirnames, filenames in os.walk(root_dir):
    print("directory:", dirpath)
    print("subdirectories:", dirnames)
    print("files:", filenames)
    print()
