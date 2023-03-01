### Task 1

User is going to write something like a blog for their daily occasions.

Write 5 functions that can handle 5 parameters depending on what user need to read, add, overwrite, create or delete files.

- 1 - Create a new file
- 2 - Read existing file
- 3 - Update some information in a file(first read it and show the content on it, after add a new text)
- 4 - Overwrite all content in a file
- 5 - Remove existing file

Please, when typing text, use the `*` character to surround the text so that the user can see the text from the file correctly!
Work with input and output styles.

```python
import os

def createFile(fname):
    pass

def readFile(fname):
    pass

def appendFile(fname):
    pass

def overwriteFile(fname):
    pass

def removeFile(fname):
    pass


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')
```

**Input:** <br>

```txt
Option: number
File name without extention(.txt): string
Text(optional): string
```

**Output:** <br>

```txt
Text or messages
```

**Sample Input - Output**

```txt
Welcome to my blog!
What you want to do with a file?
Options(type a number):
1-Create a new file
2-Read existing file
3-Update some information in existing file
4-Overwrite all content in existing file
5-Remove existing file
Write a number(1-5): 3
Pleases provide file name(without extension, automatically will be added .txt): yo
*******************
Hi my name is John, nice to meet you!Hello again!

New update is coming!!!!

Heh

I got you!
*******************

Add the text above yo.txt:
The Last Of Us!

```

### Task 2

### Task 3

Write a Python program that takes a directory path as input and organizes the files in that directory based on their file types. The program should create subdirectories for each file type and move the files to their respective subdirectories.

For example, if the directory contains files of types .txt, .pdf, and .jpg, the program should create subdirectories named txt, pdf, and jpg and move the files with those extensions to their respective subdirectories.

- Get the directory path as input from the user
- Create a dictionary to store the file types and their corresponding subdirectories
- Iterate over the files in the directory
- For each file, get its file extension
- If the file extension is not in the dictionary, create a new subdirectory for that file type
- Move the file to the corresponding subdirectory
- Print a message indicating that the files have been organized

### Task 4

### Task 5

Write your own terminal program that is able to run user commands. The program works with files and folders.

Tasks:<br />

1. You need to put the initial directory into disk `C:/`<br />
2. Create the command `ls` or `dir` to show all the existing directories in the folder<br />
3. Make the transition between directories using the command `cd folder_path`, and `cd ..` to exit back, otherwise output Exception that the directory was not found<br />
4. Write commands for creating, deleting folders and files<br />
5. Write a command `cat file_name` that reads the file and prints the data from it<br />
6. Write an interface and logic for this task so that it looks like a standard CMD

### Task 6

### Task 7

1. Upload data from the following CSV file **scrubbed.csv**
2. Find which of the columns contains date and time information.
3. Change the date and time in the column to the following: `10/10/1949 20:30` -> `October 10 of 1949 at 08:30 PM`
4. Save the data with the updated date and time format to a new csv file **"format_scrubbed.csv"**

### Task 8

### Task 9
Problem: Write a Python program that reads a file named `input.txt`, creates a directory named `output`, and writes two output files in the `output` directory. The program should also check whether the `output` directory already exists and delete its contents if it does.

Instructions:
1. Create a file named `input.txt` with some sample text.
2. Write a Python program that reads the content of `input.txt` and writes two output files named `output1.txt` and `output2.txt` in a directory named `output`.
3. The first output file (`output1.txt`) should contain the content of `input.txt` in all uppercase letters.
4. The second output file (`output2.txt`) should contain the content of `input.txt` in all lowercase letters.
5. The program should create the `output` directory if it does not exist, and delete its contents if it already exists.
6. The program should use different modes of opening files (e.g., `w`, `r`, `a`) as appropriate.
7. The program should use the `os` module and `os.path` module to check whether the `output` directory exists and to create/delete files and directories.
8. The program should print a message on the console after each file is created.

Example output:
```
Output directory created.
Output file 1 created.
Output file 2 created.
```

Note:
- You may assume that the `input.txt` file and the `output` directory are in the current working directory.
- You can use the `os.makedirs()` function to create directories recursively.
- You can use the `os.listdir()` function to list all files in a directory.
- You can use the `os.remove()` function to delete a file.
- You can use the `os.rmdir()` function to delete an empty directory.

### Task 10

### Task 11

Write a python program that should find maximum value for the given name among several files.  
For input you should accept file names separeted by space with `.txt` extension, otherwise raise `ValueError`.  
If user do not write file names, you should read from `file1.txt`, `file2.txt`, `file3.txt`.  
If there is no name in file, return -1 for this file as value.  
For the output, you should print maximum value from files for the given files.

_Example:_

```
type file names separeted by space or press enter for all: file1.txt
name: Elodi
-1
```

```
type file names separeted by space or press enter for all:
name: Elodi
25.79053940467062
```

```
type file names separeted by space or press enter for all: file.png
name: Elodi
ValueError
```

### Task 12

### Task 13
Write a Python program that takes the name of a directory as input and finds the largest file in the directory tree rooted at the given directory. The program should print the absolute path and size of the largest file.

### Task 14

Write a Python program that reads a large log file and calculates the average response time of all requests.
