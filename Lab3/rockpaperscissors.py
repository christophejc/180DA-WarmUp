import random
import time

rock = 0
paper = 1
scissors = 2

def rps():
    aiChoice = random.randint(0,2)
    choice = input("Rock [r], Paper [p], or Scissors [s] ?\n")
    
    #assigning values to input
    if choice == "r":
        choice = rock
    elif choice == "p":
        choice = paper
    elif choice == "s":
        choice = scissors
    else:
        print("Invalid input! Try again\n")
        rps()
        exit()
    
    
    print("Rock, Paper, Scissors...\n")
    time.sleep(1)
    print("Shoot!\n\n")

# if statements (playing the game)
    if aiChoice == choice:
        print("We both chose the same one! Try again \n")
        rps()
    elif aiChoice==rock and choice == paper:
        print("Your paper covered my rock! You win \n")
    elif aiChoice==rock and choice ==scissors:
        print("My rock broke your scissors! You Lose \n")
    elif aiChoice==paper and choice ==scissors:
        print("Your scissors cut my paper! You Win \n")
    elif aiChoice==paper and choice ==rock:
        print("My paper covers your rock! You Lose \n")
    elif aiChoice==scissors and choice ==rock:
        print("Your rock broke my scissors! You Win\n")
    elif aiChoice==scissors and choice ==paper:
        print("My scissors cuts your paper! You Lose\n")

    playagain = input("Would you like to play again? [y/n] \n")
    if (playagain == "y"):
        rps()
        exit()
    else:
        print("Thanks for playing! Goodbye")
        
    return

print("Let's play Rock, Paper, Scissors!\n")
ready = input("Ready? [y/n]\n")

if (ready == "y"):
    rps()
else:
    print("I guess you're not ready for a challenge!")
    time.sleep(2)
    exit()

