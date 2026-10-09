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


def count_guess(number):
    count = 0
    if count <= 10
    return  "Either you know the secret or you got lucky!"

    if count >= 10
    return  "You should be able to do better!"
    
    count+=1
    







guess = int(input("Enter your guess: "))

print(guess_number())
