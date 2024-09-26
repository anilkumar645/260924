# number guessing game 

import random

#generate a random number between 1 and 10 
number = random.randint(1,10)

#Promt the user to guess the number 
guess = int(input("Guess a number between 1 and 10: "))

#keep prompting the user to guess until they get it right
while guess != number:
    if guess > number:
        print("Your guess is too high. Try again")
    else:
        print("Your guess is too low. Try again")
    guess = int(input("Guess a number between 1 and 10: "))

print("You guessed it! The number was", number)