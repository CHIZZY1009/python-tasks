
import random

def guess_number():
   
    
    random_number = random.randint(1,1000)

    while guess != random_number:
        if guess > random_number:
            return 'Too High'

        elif guess < random_number:
            return 'Too low'

    if guess == random_number:
        return'Congratulations! you guessed my number'







guess = int(input("Enter an integer: "))

print(guess_number())
