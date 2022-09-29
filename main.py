logo = '''
_   _____/|__| ____    __| _/  /  _____/  ____   _____  
 |    __)  |  |/    \  / __ |  /   \  ____/ __ \ /     \ 
 |     \   |  |   |  \/ /_/ |  \    \_\  \  ___/|  Y Y  \
 \___  /   |__|___|  /\____ |   \______  /\___  >__|_|  /
     \/            \/      \/          \/     \/      \/ 
     
     '''
     
print(logo)

# Importing the randint function from the random module.
from random import randint

def check_guess(guess, answer):
    """
    It takes in a guess and an answer, and prints out a message depending on whether the guess is higher
    or lower than the answer
    
    :param guess: the user's guess
    :param answer: The answer to the game
    """
    if guess > answer:
        print("You Digged too deep")
    elif guess < answer:
        print("You Digged too shallow")
    else:
        print(f"You got it! 💎💎💎💎💎💎💎💎💎 You are rich now! Go buy a Tesla!")

# Printing out the instructions for the game.
print("Find a gem 💎 in the cave!")
print("It's in between 1km and 100km away under the ground.")


# Generating a random number between 1 and 100.
answer = randint(1, 100)



guess = int(input("Make a guess how deeper it is: "))

# A while loop. It will keep running until the guess is equal to the answer.
while guess != answer:
    check_guess(guess, answer)
    guess = int(input("Make a guess how deeper it is: "))
    
    
    
    
    










