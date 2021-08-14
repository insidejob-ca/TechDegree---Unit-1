import random

def start_game():
    random_pick = random.randint(1,10)
    count = 1 # Tracking the score
    user_guess = 0 #User's random guess number, kept it purposely zero from out range of 1-10
    user_guess = int(user_guess)
    while user_guess != random_pick:
        try:
            user_guess = int(input("Enter your number for the guessing the guess game?  "))
            if user_guess not in range(1,11):
                raise ValueError("Only integers are accepted, Please try to enter number between range(1-10)")
                
        except ValueError as err:
            print("Oh no, we ran into an issue. {}.".format(err))
            break
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
        print("Current Highscore = {}".format(highscore))
        new_highscore = start_game() #To track if user beats the current highscore
        if new_highscore < highscore: # logic to update the highscore if any user beats it
            highscore = new_highscore
        else:
            highscore
    else:
        print("Game Over! Thanks again for playing Number Guessing Game!")
        break
