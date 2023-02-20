### iterators

A lot of objects support iteration
for-statement and what happens under the hood: __iter__() and __next__().
Raising StopIteration
manual iteration over the list - example
How to implement iteration?
What iterator like `list` also have? ( len() - __len__(self) , get by index [] - __getitem__(self, index), support in - __contains__(self, value) )


### generators

A problem - generating sequences of numbers as an example
One object at a time - why/when/how to implement
Creating a generator object - calling generator function
Generator - low-level protocol that the for statements uses on dicts, sets, lists, tuples etc.

Chain generator functions - data-flow pipelines: producer -> processing -> processing -> consumer
yield from
chain iterable example

Why generators - summary


### scopes

scopes: built-in -> global -> enclosing -> local. Some examples and how to change global variable from being in function



### modules

modules and import: module - any python source file
import - loads and executes a module
namespace - module consists of functions and variables. Module name is used as prefix => namespace ( ex: program => program.py )
Modules are isolated - define same variable in two different files
Module execution - during import, until the end of the file is reached
import as - change name of a module
from - makes available locally
looking for modules - sys.path. Usually current working directory - first
python main module - python has no main function or method. The main module is the source file that runs first
__main__ check - if __name__ == '__main__'. __name__ - name of the module, become __main__ if you will try to execute like python program.py
common program template - python


### dates
datetime module - manipulating dates and times

several types of core objects:
    timedelta - represents a duration, difference between two dates or times
    datetime - single object containing all the information from a date object and a time object

create datetime and timedelta objects
compare datetime objects
converting from string to datetime and vice versa


### math
math module - mathematical functions


### json
          serial  encode          decode   deserial
python -> text -> bytes -> run -> bytes -> text -> swift


python         json
dict        -> object
list, tuple -> array
str         -> string
int, float  -> number
True        -> true
False       -> false
None        -> null

functions:
dump/dumps - serialize object into json ( to string )
load/loads - deserialize text/binary into PyObject
decode/encode - decode/encode between python/json.
JSONDecoder/JsonEncoder - could use to make objects serializable/deserializable
