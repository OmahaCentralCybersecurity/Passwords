'''
DictionaryAttack.py models a simple dictionary attack on a pretend login system.

Two txt files will be used to perform this attack.  

1. In Dec 2009, a company named Rockyou experienced a data breach where 32 million user accounts were exposed. This is 1 million of them. 

2. 370,000 common English words. 
'''
import time

## change me depending on which file you want to access. 
test = 'pa$$word11111'

filepath = '1MillionPassword.txt'

start = time.time()
attempts = 1
found = False

with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        password = line.strip()
        
        if(password == test):
            found = True
            break
        else: 
            pass

        attempts+=1
    

end = time.time()
total = end - start

if found:
    print("it took %d attempts in %f seconds to find %s" %(attempts, total, password))
else:
    print("password not found")
            
