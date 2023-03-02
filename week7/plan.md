### 3 parts: work with directory and files & built-in functions &

-- example 1
`open(filename, mode, encoding)` - to open files
f = open('filename')

open modes = ['r', 'w', 'a', 'r+']
r - read
w - write
a - append
r+ - both read and write

-- example 2
example: f = open('filename', 'w')
`write(text)` - add text into file; example - f.write('some text')
`close()` - to close files; example - f.close(); important to close files; you couldn't read closed file


-- example 3
`f.read()` - to read the entire file
`f.readline()` - read only one line from file
`f.readlines()` - to read all lines from file as list


-- example 4
### recommended approach to work with files/close files
context manager
```python
with open('filename') as f:
    print(f.read())
```

-- example 5
### Libraries
every library in python is module
libraries - built-in and external


-- example 6
### os module
low-level API to work/interact with your system. Files, directories, processes, rights


methods
os.environ - mapping object, where keys and values are strings that represent the process environment
os.environ['HOME'] - pathname of your home directory
mapping is captured the first time the os module is imported


-- example 7
os.getcwd() - get current working directory ( string )
os.chdir(path) - change the current working directory to path
os.listdir(path) - returns a list of all the files and directories in the path specified


-- example 8
os.mkdir(path) - create a directory named path; if directory exists - FileExistsError; if a parent directory in the path doesn't exist,
FileNotFoundError is raised
os.makedirs(name) - recursive directory creation, like mkdir(), but makes all intermediate directories
os.rmdir(path) - This method removes the directory at the path specified.


-- example 9
os.path.exists(path) - returns True if the file or directory at the specified path exists, and False otherwise.
os.remove(path) - removes the file at the path specified.
os.path.abspath(path) - returns the absolute path of the specified path
os.path.join(path1, path2, ...) - joins two or more path components into a single path


-- example 10
os.walk(path) - traverse a directory
```python
import os

root_dir = "/path/to/root/directory"
for dirpath, dirnames, filenames in os.walk(root_dir):
    print("directory:", dirpath)
    print("subdirectories:", dirnames)
    print("files:", filenames)
```


### shutil
high-level API to work with files and directories

-- example 11
shutil.copy('/path/to/source/file', '/path/to/destination/file') - copy a file from one location to another
shutil.copytree('/path/to/source/directory', '/path/to/destination/directory') - copy an entire directory and all the content
shutil.move('/path/to/source/file', '/path/to/destination/file') - to move a file or directory or to rename


-- example 12
shutil.rmtree('/path/to/directory/to/delete') - to delete a directory and all its contents
shutil.make_archive('/path/to/destination/archive', 'zip', '/path/to/source/directory') - to create a compressed archive file (such as a zip or tar file) of a directory and all its contents


-- example 13
os.path.isdir(path) - to check if a path points to a directory
os.path.isfile(path) - check if a path points to a file


### work with exceptions
a way for Python to indicate that something has gone wrong during the execution of a program
When an exception is raised, the program stops running and Python display an error message that describes the exception


-- example 14 - raise an Exception ( for example raise ValueError if user entered not number )
```python
try:
    x = int("not an integer")
except ValueError:
    print("Invalid input")
```


-- example 15 - Handling an exception & handle multitple exceptions
try except block
try block - contains the code that might raise an exception
except block - code that should run if an exception is raised
try:
    x = int("not an integer")
except ValueError:
    print("Invalid input")


try:
    x = 1 / 0
except (ZeroDivisionError, TypeError):
    print("Error: division by zero or invalid type")


-- example 16; optional block - finally
try:
    f = open('')
finally:



-- example 17; optional block - else
```python
try:
    number = 5
    div = int(input())
    print(number / 5)
except (ZeroDivisionError, ValueError):
    print('enter correct number')
else:
    print('everything is ok')
finally:
    print('the end')
```

-- example 18; creating custom exceptions
```python
class CustomException(Exception):
    pass
```

fluent-python;
Docker
Python - generators, parser/framework ( django/fastapi/aiohttp, flask ), exceptions
pytelegram/aiogram
-- async/await, GIL 
Git
OOP - основные концепции ( inh/poly/abst/incaps )

