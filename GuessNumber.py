import random

num = random.randrange(25)

guess = int(input('Guess a number between 0 and 25: '))

while guess != num:
    if guess < num:
        guess = int(input('Too low, try again: '))
    elif guess > num:
        guess = int(input('Too high, try again: '))

print('Congrats! You won!')