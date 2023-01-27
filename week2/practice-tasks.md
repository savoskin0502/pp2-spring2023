### Task 1

You are given products. Split the products on a " " (space) delimiter and join using a ", " comma. Add results to this sentence and print it: I have `products` in my shopping cart.

<b>NOTE:</b> use string methods and string formatter.

<b>Input Format:</b>
The one line contains a string consisting of space separated words.

<b>Prints:</b>
string: resulting string in the sentence.

<b>Sample Input:</b>

```
apple candy grapes banana
```

<b>Sample Output:</b>
I have apple, candy, grapes, banana in my shopping cart.

### Task 2

You have a non-empty set s, and you have to execute N commands given in N lines. `a = [1, 2, 3, 4, 5, 6, 7, 8, 9]` <br>
The commands will be `pop`, `remove` and `discard`.

<b>NOTE:</b> use set with pop, remove and discard.

<b>Input Format:</b>
The first line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

<b>Prints:</b>
Print the sum of the elements of set s on a single line.

<b>Sample Input:</b> `a = [1, 2, 3, 4, 5, 6, 7, 8, 9]`

```
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
```

<b>Sample Output:</b>
4

### Task 3

Print all exact squares of natural numbers not exceeding the given number N

Input: integer `N`

Output: squares of natural numbers not exceeding N

For example: N = 15; => 1, 4, 9

### Task 4

Given string `S` that contains sentence or just a words separated by space.
Print each word with count of its appearance in `S`

Input: string `S`

Output: dictionary `word : count`

### Task 5

Make a quiz game that can have one or multiple answers to the questions (using a dictionary, set). The user will be asked to answer to the several questions by input. If the user got less than `70%` correctness, the user loses. If more than `70%`, the user wins.

<b>Input:</b> user inputs answers to the questions

<b>Output:</b> if the user wins output `Congrats!`, else `You lost!`

<b>Sample input 1:</b>
1. Which is the currency of Kazakhstan? Tenge
2. Name one of the past/present presidents of Kazakhstan: Tokayev
3. What year Kazakhstan proclaim independence? 1991

<b>Sample output 1:</b> Congrats, you won with 100.00% correctness

<b>Sample input 2:</b>
1. Which is the currency of Kazakhstan? KZT  
2. Name one of the past/present presidents of Kazakhstan: Nazarbayev
3. What year Kazakhstan proclaim independence? 1986

<b>Sample output 2:</b>
You lost! You got only 66.67% correctness

### Task 6

Given a list of tuples. Every tuple contains `2` values. Write a program that multiplies values in every tuple.

<b>Input:</b> a list of tuples

<b>Output:</b> a list containing multiplication results of the tuples

<b>Example:</b> Given `[(1,2), (2,3), (3,7), (4,16)]`. Result will be `[2, 6, 21, 64]`

### Task 7

Create an empty list, and then add to this list all the numbers from 1 to 100 that are divisible by 3 (without remiander)

Expected results: `[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60,
63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]`

### Task 8

You are given a list `arr2 = [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktau"]`, whose elements are different types(integer, string, etc.). Use loop to solve all problems.

from `arr2` to new empty list `only_ints` add only elements have type `int`

from `arr2` to new empty list `list_of_string` add only elements have type `str`

from `arr2` to new empty list `float_nums` add only elements have type `float`

from `arr2` to new empty list `array_of_bools` add only elements have type `bool`

only_ints = []

list_of_string = []

float_nums = []

array_of_bools = []

print(only_ints)

print(list_of_strings)

print(float_nums)

print(array_of_bools)

Expected results: 

`[100, -10, 1, 3, 4, 70, 24, -9]`

`['Astana', 'Almaty', 'Aktau']`

`[10.4]`

`[True]`

### Task 9

You are asked to help teacher to evaluate average grade of students. Given list of tuples consisting name of student() and the grade. 
You need calculate average grade of each student and print them.

<b>Input Format:</b>

The first line contains integer N, the number of tuples.

The next N lines contains student name and grade separated by space, where name is string and grade is integer between 0 and 100 included.

<b>Output Format:</b>

Print on each line name of student and average grade rounded to integer

<b>Sample Input:</b>
```
4
Erlan 90
Arsen 100
Arsen 80
Erlan 80
```
<b>Sample Output:</b>
```
Erlan 85
Arsen 90
```
### Task 10

You are given a word. Count the number of each letter in the word.

<b>Sample Input</b>:
```
International
```
<b>Sample Output</b>:
```
i 2
n 3
t 2
e 1
r 1
a 2
o 1
l 1
```
### Task 11

You are given a positive integer `number`, print numbers from 1 to number.<br/>
If the number is multiple of 3, print `Fizz`, if the number is multiple of 5, print `Buzz`, if the number is multiple of 3 and 5, print `FizzBuzz`.<br/>
<b>Note</b>: output must end with ".", only 10 numbers in a row and all numbers must be separeted by "," and right-aligned.

<b>Example:</b>

<b>Input:</b> `number = 100`

<b>Output:</b>

```
       1,        2,     Fizz,        4,     Buzz,     Fizz,        7,        8,     Fizz,     Buzz, 
      11,     Fizz,       13,       14, FizzBuzz,       16,       17,     Fizz,       19,     Buzz, 
    Fizz,       22,       23,     Fizz,     Buzz,       26,     Fizz,       28,       29, FizzBuzz,
      31,       32,     Fizz,       34,     Buzz,     Fizz,       37,       38,     Fizz,     Buzz,
      41,     Fizz,       43,       44, FizzBuzz,       46,       47,     Fizz,       49,     Buzz,
    Fizz,       52,       53,     Fizz,     Buzz,       56,     Fizz,       58,       59, FizzBuzz,
      61,       62,     Fizz,       64,     Buzz,     Fizz,       67,       68,     Fizz,     Buzz,
      71,     Fizz,       73,       74, FizzBuzz,       76,       77,     Fizz,       79,     Buzz,
    Fizz,       82,       83,     Fizz,     Buzz,       86,     Fizz,       88,       89, FizzBuzz,
      91,       92,     Fizz,       94,     Buzz,     Fizz,       97,       98,     Fizz,     Buzz.
```

### Task 12

You are given a positive integer n.<br/>
You have n pair, for each pair you have key - type and value.<br/>
If key - `str`, you add value into array.<br/>
If key - `bool`, you sort array. If value - True, in ascending order, value - False, in descending order.<br/>
If key - `int`, you take sublist of array from value index. If index is invalid, do nothing.<br/>
If key - `set`, you add value into array, then remove all duplicates.<br/>
Otherwise, add key at the start of the array and value at the end of the array.<br/>

<b>Example:</b>

<b>Input:</b>

```
6
str Hello  
float 1.5 
set float
dict None  
bool False
int 2
```

<b>Output:</b> `['None', 'Hello', '1.5']`
