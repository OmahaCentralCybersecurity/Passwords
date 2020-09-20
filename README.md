# Passwords
Create a random password generator and then use various methods to crack it.  

## Random Password Generator
Create a Python program that generates a password of random letters and characters. Include lowercase, uppercase and digits and optionally, puncutation.  

Instead of intializing a string or list that contains them, python has library `string` that can be imported.  Some of the functions that `string` includes is:

`string.ascii_letters`: The concatenation of the ascii_lowercase and ascii_uppercase constants.  
`string.ascii_lowercase:` All lowercase letters
`string.digits`: '0123456789'  
`string.puncuation`: all characters considered to be puncuation.  

```
import string

letters = string.ascii_lowercase

```

## Directions for `PasswordGenerate.py`  
- Create a function `generate` that has parameter of length that determines the length of the password. 
- Your function should include all letters and digits (optionally include punctuation)
- It should randomly pick from available characters. 
- Test `generate` by prompting for user input

---

# Password Attack Lab
In this lab you will test two common methods to password cracking: brute force and a dictionary attack. In both you will adjust values within the code and note the change it has upon the program's ability to crack a password.  

## Brute Force  
Instructions:
1. Use your password generator - or - the one that is provided.  `generate()` is called in `BruteForce.py`, you may change that function call.  You will have to also change the import statement.  
2. Look up the `itertools` documenation 
3. Run `BruteForce.py` a couple of times, changing the number of random characters in your password.  Note time taken given a certain number of characters and the number of guesses.  Try password lengths of 2, 3, 4, and 5. Run multiple tests.
4. Change 
5. How many guesses per second is your computer making? 
6. What is the number of guesses needed to brute-force all 2, 3, 4 and 5 character passwords?
7. Based on the time taken for the lengths of 2 - 5, how long would estimate it would take to brute-force a 6 character password? 7? 8? 
8. 


## Dictionary Attack  
h/t [fendy Hackernoon article](https://hackernoon.com/i-cracked-40000-passwords-with-python-yours-might-have-been-one-of-them-3fr32je)





