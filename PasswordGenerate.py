import string, random

# generate should take a length and the return a password of random letters and digits. Puncuation is optional. 

def generate(length):
    characters = string.ascii_lowercase + string.ascii_uppercase # + string.digits
    create_password = ''
  
    for i in range(length):
        rand = random.randint(0, len(characters)- 1)
        create_password = create_password + characters[rand]
    
    return create_password



