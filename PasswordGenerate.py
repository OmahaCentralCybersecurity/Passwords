import string, random

# generate should take a length and the return a password of random letters and digits. Puncuation is optional. 

def generate(length):
  characters = string.ascii_letters + string.digits
  password = ''
  
  for i in range(length):
    rand = random.randint(0, len(characters))
    password = password + characters[rand]
    return password

generate()


