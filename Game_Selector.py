import Gibbet
import Guessing_Game

def Game_Selector():

    print("****************************")
    print("******Chose your Game*******")
    print("****************************")

    print("(1) Guessing Game; (2) Gibbet Game; (exit) Exit Game Selector")

    Game = input("Chose a game: ")
    
    Choice = False
    
    if Game == "exit": 
        Choice = True
        print("Exiting the Game Selector...")
    else:
        Game = int(Game)

    while Choice == False:
        if Game == 1:
            print("Loading Guessing Game...")
            Guessing_Game.Play_Guessing()
            Choice = True
        elif Game == 2:
            print("Loading Gibbet Game...")
            Gibbet.Play_Gibbet()
            Choice = True
        else:
            print(f"The number {Game} isn't a Game.")

if (__name__ == "__main__"):
    Game_Selector()