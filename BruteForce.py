from PasswordGenerate import generate
import string, itertools
import time

def brute_force(passLen, password):

    start_time = time.time()

    guess = ""
    correct = False

    ### Change me to try various character combinations
    characters = string.ascii_lowercase + string.ascii_uppercase

    for letters in itertools.product(characters, repeat = passLen):
        # letter is formatted as ('char', 'char') so use .join to create one string. 
        letters = ''.join(letters)
        #print(letters)
        if letters == password:
            guess = letters
    
    end_time = time.time()
    total_time = end_time - start_time
    return guess, total_time


#program
# prompt user for password length and then generate a random sequence of the given length 
passLen =  int(input("How many characters for your password?: "))
generated_password = generate(passLen)
print(generated_password)
guessed_pwd, time_taken = brute_force(passLen, generated_password)

print("The password",guessed_pwd, "took", time_taken, " seconds to guess. ")


