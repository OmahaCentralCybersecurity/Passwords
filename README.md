# Passwords
Create a random password generator and then use various methods to crack it.  

## Random Password Generator
Create a Python program that generates a password of random letters and characters.  For simplicity we will make our first password generator take only lower case letters. We can eventually add on uppercase, digits and puncuation.  

Instead of intializing a string or list that contains them, python has library `string` that can be imported.  Some of the functions that `string` includes is:

`string.ascii_letters`: The concatenation of the ascii_lowercase and ascii_uppercase constants.  
`string.ascii_lowercase:` All lowercase letters
`string.digits`: '0123456789'  
`string.puncuation`: all characters considered to be puncuation.  

```
import string

letters = string.ascii_lowercase

```

## Directions:
- Create a function `generate` that has parameter of length that determines the length.  
- Call `generate` and test your outputs.  

- Test your random passwords by importing and using the file: PasswordCracker.py
- Note the time it takes for given password lengths ... there might not be enough time ...


Questions:  


