import random
print("------------------------------------ \n Welcome to Number Guessing Game \n------------------------------------")


def start_game():
    answer = random.randint(1,10)
    print(answer)
    count = 1
    guess = 0
      
    while guess != answer:
        try:
            guess = int(input("Enter your value for the guessing the guess?  "))
            if guess not in range(1,10):
                
#                raise ValueError("Please try to enter value between 1-10")
                continue
        except ValueError:
            print("Oh no, we ran into an issue. {}. Please try again within the range 1-10")
        else:
            if guess > answer:
                count +=1
                print("It's lower")
            elif guess < answer:
                count +=1
                print("It's higher")
    else:
        print("you got it in {}.".format(count))
        continuing = input("if you want to continue playing? Y/N?  ")
        if continuing.lower() == "y":
            start_game()
        else:
            print("Thanks again for playing Number Guessing Game")
    return count

start_game()
