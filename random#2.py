#guess the number game using a for loop

#imports the ability to get a random number (we will learn more about this later!)
from random import *

numberOfGuesses=0
#Generates a random integer.
aRandomNumber=randint(1, 20)
print("The random number (secret) is: ", aRandomNumber)
# For Testing: print(aRandomNumber)

for i in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if (int(guess)!=aRandomNumber):
        if not guess.isnumeric(): # checks if a string is only digits 0 to 9
            print("That's not a positive whole number, try again!")
        else:
            if int(guess)<(aRandomNumber):
                print("Guess higher")
            if int(guess)>(aRandomNumber):
                print("Guess lower")
    else:
        print("Yay you guessed it!")
