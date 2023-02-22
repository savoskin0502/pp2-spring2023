### Task 1

Write a Python function that extracts user input and searches `text-paypal.py` for a matching one. The program should output all matching inputs in the form of a sentence (the sentence ends with a dot ( . )).<br><br>
When entering user data, provide 3 input options. Answers must be true(True) or false(False)

- It looks for sentences where it starts with user input. (^)
- It looks for sentences where it ends with user input. ($)
- It contains a number in it? (\d)

<i>NOTE: Use only regular expression!
HINT: use split, search methods of regex</i>

**Input:** <br>
String: Word that you want to search
Bool element(^): True or False (lower or upper cases when checked in a code)
Bool element($): True or False (lower or upper cases when checked in a code)
Bool element(\d): True or False (lower or upper cases when checked in a code)

**Output:** <br>
Return sentences that matched the conditions.

**Sample Input(1):**

```
Please write the keyword which we should search: Pay
It looks for sentences where it starts with user input: True
It looks for sentences where it ends with user input: False
It contains a number in it? False
PayPal history: looking back at the milestones

```

**Sample Output(1):**

```
PayPal is one of the largest online payment processors in the world
PayPal history boasts a successful timeline of growth and innovation, becoming the desired way to pay for many
PayPal’s history has been steeped in strategic moves that have produced impressive revenue and a large customer base
PayPal history reveals that the company knows how to accelerate its growth and deliver a seamless service to its customers
```

**Sample Input(2):**

```
Please write the keyword which we should search: Pay
It looks for sentences where it starts with user input: True
It looks for sentences where it ends with user input: False
It contains a number in it? True

```

**Sample Output(2):**

```
PayPal history: the beginning PayPal history begins back in 1998 when it was established as Confinity by Max Levchin and Peter Theil
PayPal spun out of eBay in 2015
PayPal will now have an in-store presence in 11 markets across Europe and Latin America
```

### Task 2

### Task 3

Write a Python function that validates a user's email address according to the following requirements:

- The email address must contain a username and a domain separated by an "@" symbol.
- The username may contain letters (both uppercase and lowercase), numbers, dots, and hyphens.
- The domain may contain letters (both uppercase and lowercase) and hyphens.
- The domain must end with a valid top-level domain, such as ".com", ".org", ".kz" and so on.

### Task 4

### Task 5

You are given information about 20 restaurants in `restaurants` dictionary from `data.py` file.<br />Your goal is to write a function that converts `restaurants` dictionary as follows:<br />

```
result = {
    0: {
        restaurants_restaurant_R_res_id: 16668008
        restaurants_restaurant_apikey: 10a35f36f5898432823df42bc743c8aa
        restaurants_restaurant_id: 16668008
        restaurants_restaurant_name: Arigato Sushi
        ...
    },
    1: {
        restaurants_restaurant_R_res_id: 801690
        restaurants_restaurant_apikey: 10a35f36f5898432823df42bc743c8aa
        restaurants_restaurant_id: 801690
        restaurants_restaurant_name: Mocha
        ...
    },
    ...
    19: {
        ...
    }
}
```

with all information.<br />Result is a nested dictionary: <br />- key is a number of restaurant<br />- value is a dictionary containing information about the restaurant that has keys according to the `ids` list from `data.py` file.<br />
NOTE: use Regex methods in this exercise.

### Task 6

### Task 7

Image you are machine learning engineer. You should preprocessing data (cleaning from unnecessary characters) in order to classificate messages to spam or not spam. You have a list of messages in `text.py`

What should you do:

1. cleaning messages from unnecessary characters `[",",  ".", ";" .............]`
2. convert all messages to lower words `str.lower()`
3. delete all spaces that are more > 1 and the last space from string `str.rstrip()`
4. use function `map` to delete unwanted space `map(function that delete unwanted space, iterable object)`

`Note` You can use library re in order to solve this problem.

**Expected result**

`['go until jurong point crazy available only in bugis n great world la e buffet cine there got amore wat', 'ok lar joking wif u oni', 'free entry in 2 a wkly comp to win fa cup final tkts 21st may 2005 text fa to 87121 to receive entry question std txt rate t c s apply 08452810075over18 s', 'u dun say so early hor u c already then say', 'nah i don t think he goes to usf he lives around here though', 'freemsg hey there darling it s been 3 week s now and no word back i d like some fun you up for it still tb ok xxx std chgs to send £1 50 to rcv', 'even my brother is not like to speak with me they treat me like aids patent', 'as per your request melle melle oru minnaminunginte nurungu vettam has been set as your callertune for all callers press 9 to copy your friends callertune', 'winner as a valued network customer you have been selected to receivea £900 prize reward to claim call 09061701461 claim code kl341 valid 12 hours only', 'had your mobile 11 months or more u r entitled to update to the latest colour mobiles with camera for free call the mobile update co free on 08002986030', 'i m gonna be home soon and i don t want to talk about this stuff anymore tonight k i ve cried enough today', 'six chances to win cash from 100 to 20 000 pounds txt csh11 and send to 87575 cost 150p day 6days 16 tsandcs apply reply hl 4 info', 'urgent you have won a 1 week free membership in our £100 000 prize jackpot txt the word claim to no 81010 t c www dbuk net lccltd pobox 4403ldnw1a7rw18', 'i ve been searching for the right words to thank you for this breather i promise i wont take your help for granted and will fulfil my promise you have been wonderful and a blessing at all times', 'i have a date on sunday with will', 'xxxmobilemovieclub to use your credit click the wap link in the next txt message or click here http wap xxxmobilemovieclub com n qjkgighjjgcbl', 'oh k i m watching here', 'eh u remember how 2 spell his name yes i did he v naughty make until i v wet', 'fine if that the way u feel that the way its gota b', 'england v macedonia dont miss the goals team news txt ur national team to 87077 eg england to 87077 try wales scotland 4txt ú1 20 poboxox36504w45wq 16']`

### Task 8

### Task 9

### Task 10

### Task 11

You are given a string `movies` inside `movies.py`.  
In this task you should write a python program that reads all movies in `movies`.  
User can enter regular expression in order to find how many movies matches with this expression.  
In addition, user can enter `list` to see all movies.

_Note:_ all movies must be without quotation mark.  
_Note:_ you should not use `split()`

**Example**

```
The default regular expresion is any symbol
Enter `exit` to finish or `list` to see all movies
Enter a regular expression (or press ENTER to use the default`): The
found 54 movie(s): The Shawshank Redemption, ...
Enter a regular expression (or press ENTER to use the default`): Ro*
found 14 movie(s): Rear Window, ...
Enter a regular expression (or press ENTER to use the default`): Ro+
found 4 movie(s): Rocky, ...
Enter a regular expression (or press ENTER to use the default`): exit
Exit...
```

**Example**

```
The default regular expresion is any symbol
Enter `exit` to finish or `list` to see all movies
Enter a regular expression (or press ENTER to use the default`): list
The Shawshank Redemption
The Godfather
Part II
Pulp Fiction
Inception
...
```

### Task 12

### Task 13

### Task 14