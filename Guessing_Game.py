# importing the random library for the number and the time for the thriller time 
import random
import time

print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

# exit variable
exit = False

# points variable
point = 0

# Creating a while structure so the user can quit it
while exit == False:
    
    time.sleep(0.5)
    
    # getting a random number
    number = random.randint(1,10)
    
    # creating an input to the user put the number 
    guess = int(input("Input your number from 1 to 10(Input 0 if you want to exit): "))
    
    # defining the exit command
    if guess == 0: 
        exit = True
        print("Exiting the Game...")
        break
    
    # defining the variables that will be used in the conditionals
    right = number == guess and 0 < guess <= 10 
    higher = number < guess and 0 < guess <= 10
    lower = number > guess and 0 < guess <= 10
    
    # creating a time for thriller
    time.sleep(0.5)

    # printing the number that the user guessed to confirm and thriller
    if guess > 0: print(f"You Guessed the number {guess}...")
    # you can use the f before the "", and then in the {} you put the variable that you want
    # that's to save time and to make less and prettier code

    # another time for thriller
    time.sleep(1.4)

    # Creating a delimitation on the answer
    print("****************************")
    
    # creating a conditional to see if the guessed number was right and printing it
    if right:
        print(f"You found it! The number was {number}.") 
        point += 1
    elif lower:
        print(f"You failed! The number was {number}, your guess was lower than that.")
        point -= 1
    elif higher:
        print(f"You failed! The number was {number}, your guess was higher than that.")
        point -= 1
    elif guess > 10:
        print(f"The number {guess} isn't betwen 1 and 10.")
        
    print('****************************')
    
    time.sleep(0.5)
    
    # Creating a Game over system 
    if point == -3: exit = True and print("Game Over")
    

time.sleep(0.5)

# Creating a code to show the points
if point <= 0: print("You didn't make any points!")
else: print(f"You made {point} points")