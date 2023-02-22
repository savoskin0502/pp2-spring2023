### intro regex  

regex - for text matching, search patterns  
re - module in python to use regexes in python  


### matching characters  
most letters - match themselves ( for ex test will match test exactly )
some characters - metacharacters ( don't match themselves ). Characters: . ^ $ * + ? { } [ ] \ | ( )  


### performing matching  
> `match()` - determine if the RE matches at the beginning of the string.  
> `search()` - scan through a string, looking for any location where this RE matches.  
> `findall()` - find all substrings where the RE matches, and returns them as a list.    
> `finditer()` - find all substrings where the RE matches, and returns them as an iterator.    


### To query match object  
> `group()` - return the string matched by the RE  
> `start()` - Return the starting position of the match  
> `end()` - return the ending position of the match  
> `span()` - return a tuple containing the (start, end) positions of the match  


### probably usable pattern  
```python
import re

p = re.compile( ... )  
m = p.match( 'string goes here' )  

if m:  
    print('Match found: ', m.group())  
else:
    print('No match')
```

###   

ASCII, A Makes several escapes like \w, \b, \s and \d match only on ASCII characters with  
the respective property.  
DOTALL, S Make . match any character, including newlines.  
IGNORECASE, I Do case-insensitive matches.  
LOCALE, L Do a locale-aware match.  
MULTILINE, M Multi-line matching, affecting ^ and $.  
VERBOSE, X (for ‘extended’) Enable verbose REs, which can be organized more cleanly and understandably  
