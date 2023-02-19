# importing the random library for the number and the time for the thriller time 
import random
import time

# getting a random number
number = random.randint(1,10)

print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

# creating the input to the user guess the number 
guess = int(input("Input your number from 1 to 10: "))

# creating a time for thriller
time.sleep(1)

# printing the number that the user guessed to confirm and thriller
print(f"You Guessed the number {guess}...")
# you can use the f before the "", and then in the {} you put the variable that you want
# that's to save time and to make less and prettier code

# another time for thriller
time.sleep(2)

# creating a conditional to see if the guessed number was right and printing it
if number == guess: print(f"You found it! The number was {number}!")
else: print(f"You failed! The number was {number}!")
# minimal conditional to save code lines and prettier code(in my opinion)
