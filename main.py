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

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

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
        
def set_difficulty():
    """
    It asks the user for the difficulty level and returns it
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS      

# Printing out the instructions for the game.
print("Find a gem 💎 in the cave!")
print("It's in between 1km and 100km away under the ground.")

# Calling the function `set_difficulty` and assigning the return value to the variable `turns`.
turns = set_difficulty()

print(f"You have {turns} turns to find the gem.")

# Generating a random number between 1 and 100.
answer = randint(1, 100)
guess = int(input("Make a guess how deeper it is: "))



# A while loop that checks if the guess is not equal to the answer. If it is not, it subtracts 1 from
# the turns variable. Then it checks if the turns variable is equal to 0. If it is, it prints out a
# message and breaks out of the loop. If it is not, it prints out the number of turns left and asks
# the user for a guess. Then it calls the `check_guess` function.
while guess != answer:
    turns -= 1
    if turns == 0:
        print("You ran out of turns, you lose.")
        break
    print(f"You have {turns} turns left.")
    guess = int(input("Make a guess: "))
    check_guess(guess, answer)
