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


## Dictionary Attack  
h/t [fendy Hackernoon article](https://hackernoon.com/i-cracked-40000-passwords-with-python-yours-might-have-been-one-of-them-3fr32je)





