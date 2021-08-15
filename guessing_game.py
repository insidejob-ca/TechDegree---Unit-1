"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

print("-----------------------------------\n  Welcome to Number Guessing Game  \n-----------------------------------")

def start_game():
    random_pick = random.randint(1,10)
    count = 1 # Tracking the score
    user_guess = 0 #User's random guess number, kept it purposely zero from out range of 1-10      
    while user_guess != random_pick:
        try:
            user_guess = int(input("Enter your number for the guessing the guess game?  "))
            if user_guess not in range(1,11):
                print("Please try to enter integers number between range(1-10).")
                continue          
        except ValueError:
            print("Oh no, we ran into an issue, Please try again with integers only in the range(1-10).")
        else:
            if user_guess > random_pick:
                count +=1
                print("It's lower")
            elif user_guess < random_pick:
                count +=1
                print("It's higher")
    else:
        print("Bingo, your guess is right in {} attempts.".format(count))
    return count

highscore = start_game()
print('#' * 8, "Current Highscore = {}".format(highscore), '#' * 8)

#Asking user if continue playing the game
while True: 
    user_continuing = input("if you want to continue playing? Please select Y/N?  ")
    if user_continuing.lower() == "y":
        print("^^^ Starting New Round ^^^ -- Current Highscore = {}".format(highscore))
        new_highscore = start_game() #To track if user beats the current highscore
        if new_highscore < highscore: # logic to update the highscore if any user beats it
            highscore = new_highscore
        else:
            highscore
    elif user_continuing.lower() != "y" and user_continuing.lower() != "n":
        print("Please enter Y(ES)/N(O) if you would like to continue playing!!!")
    else:
        print("Game Over! Thanks again for playing Number Guessing Game!")
        break
