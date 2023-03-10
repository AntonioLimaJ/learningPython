# importing the random library for the number and the time for the thriller time 
import random
import time
import Game_Selector

def Try_Again():
                    game = input("Want to play again?((y) yes; (n) no): ")
                    if game == "y":
                        Play_Guessing()
                    elif game == "n":
                        print("Going Back to Game Selector...")
                        Game_Selector.Game_Selector()
                    else:
                        print("The letter you pressed wasn't y or n.")
                        Try_Again()
                        
def Play_Guessing():

    print("****************************")
    print("Welcome to the Guessing Game")
    print("****************************")

    # exit variable
    exit = False

    # points variable
    point = 0

    # Set the amount of lifes
    life = 0

    # Set the while conditional
    ex_difficulty = False

    # Set the lifes to each difficulty
    while ex_difficulty == False:
        
        # Put the choice of the difficulty
        in_difficulty = int(input("Chose the difficulty(1 to easy, 2 to medium and 3 to hard): "))
        
        if in_difficulty == 1: 
            life += 5
            ex_difficulty = True
        elif in_difficulty == 2: 
            life += 3
            ex_difficulty = True
        elif in_difficulty == 3: 
            life += 1
            ex_difficulty = True
        else: print(f"The number {in_difficulty} isn't a difficulty.")

    # Creating a while structure so the user can quit it
    while exit == False:
        # A For structure to the lifes
        for chance in range(0, life):
            
            #shows the life for the user
            print(f"Life: {life}")
            
            #shows the Points for the user
            print(f"Points: {point}")
            
            time.sleep(0.5)
            
            # getting a random number
            number = random.randint(1,10)
            
            # creating an input to the user put the number 
            guess = input("Input your number from 1 to 10(Input exit if you want to leave): ")
            
            # defining the exit command
            if guess == "exit": 
                exit = True
                print("Exiting the Game...")
                break
            else:
                guess = int(guess)
            
            # defining the variables that will be used in the conditionals
            right = number == guess and 1 <= guess <= 10 
            higher = number < guess and 1 <= guess <= 10
            lower = number > guess and 1 <= guess <= 10
            
            time.sleep(0.2)

            # printing the number that the user guessed to confirm and thriller
            print(f"You Guessed the number {guess}...")
            # you can use the f before the "", and then in the {} you put the variable that you want
            # that's to save time and to make less and prettier code

            # another time for thriller
            time.sleep(1)

            # Creating a delimitation on the answer
            print("****************************")
            
            # creating a conditional to see if the guessed number was right and printing it
            # this conditional add or remove points and reduce the life if the user is wrong
            if right:
                print(f"You found it! The number was {number}.") 
                point += 1
                chance -= 1
            elif lower:
                print(f"You failed! The number was {number}, your guess was lower than that.")            
                life -= 1
            elif higher:
                print(f"You failed! The number was {number}, your guess was higher than that.")
                life -= 1
            else:
                print(f"The number {guess} isn't betwen 1 and 10.")
                chance -= 1
                
            print('****************************')
            
            time.sleep(0.5)
            
            if life == 0:
                Try_Again()
                
    time.sleep(0.5)

    # Creating a code to show the points
    if point <= 0: print("You didn't make any points!")
    else: print(f"You made {point} points")