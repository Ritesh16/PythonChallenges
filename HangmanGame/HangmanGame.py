import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

lives = 6

# word_list = ["delaware", "burger", "gatlinburg"]

random_word = random.choice(word_list)

print(logo)

display = []
random_word_length = len(random_word)
for _ in range(random_word_length):
    display += "_"

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()
    clear = lambda: os.system("cls")
    clear()
    if guess in display:
        print(f"You have already guessed letter {guess}")

    for position in range(random_word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        print(f"You guessed letter {guess}, that's not in the word. You lose a life'")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])