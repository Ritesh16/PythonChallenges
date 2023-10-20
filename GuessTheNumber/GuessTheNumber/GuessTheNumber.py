import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 & 100.")
difficultyLevel = input("Choose difficulty level. Type 'easy' or 'hard': ")
attempts = 5

if difficultyLevel == "hard":
    attempts = 10

randomNumber = random.choice(range(1, 100))
print(f"answer is {randomNumber}")

while attempts > 0:
    print(f"You have {attempts} attempts to guess the number")
    answer = int(input("Make a guess."))
    if answer > randomNumber:
        print("Too High!")
    elif answer < randomNumber:
        print("Too Low!")
    else:
        print("Your guess is correct: You win!!!!!")
        break
    attempts-=1
    if attempts > 0:
        print("Guess again.")

if attempts == 0 :
    print("You lost. Ending game....")
