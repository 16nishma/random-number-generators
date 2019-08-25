#guess the number game using while loop

#imports the ability to get a random number (we will learn more about this later!)
from random import *

numberOfGuesses=0
#Generates a random integer.
aRandomNumber=randint(1, 20)
print("The random number (secret) is: ", aRandomNumber)
# For Testing: print(aRandomNumber)

while (numberOfGuesses<=2):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if (guess!=aRandomNumber):
        if not guess.isnumeric(): # checks if a string is only digits 0 to 9
            print("That's not a positive whole number, try again!")
        else:
            guess=int(guess) # converts a string to an integer
            numberOfGuesses += 1
            if guess<aRandomNumber:
                print("Try guessing higher!")
            if guess>aRandomNumber:
                print("Try guessing lower!")
    if guess==aRandomNumber:
        print("You guessed it right!")
        break
