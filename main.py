# Day 7 – Hangman Game
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Building a full game loop using while
# - Tracking game state with variables
# - Working with lists and strings together
# - Iterating using indexes
# - Managing lives and win/lose conditions
# - Importing and using external modules and assets
#
# This project represents my first complete word-guessing game
# with multiple states, feedback, and visuals.

import random
from art import stages, logo, welcome
from hangman_words import word_list

# Display welcome message and game logo
print(welcome)
print(logo)

# Randomly select word from the word list
chosen_word = random.choice(word_list)
print(f"Psst. the chosen word is {chosen_word}")

# Create placeholder with underscores
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)

# Convert placeholder string to list for easy updates
display = list(placeholder)

game_on = True
user_lives = 6

# Main game loop
while game_on:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Handle repeated guesses
    if guess in display:
        print(f"You've already guessed {guess}")

    # Handle incorrect guesses
    elif guess not in chosen_word:
        user_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

    # Handle correct guesses
    else:
        print(f"You guessed {guess}")
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess

    # Display current game state
    print("".join(display))
    print(stages[user_lives])
    print(f"You have {user_lives} lives left")

    # Losing condition
    if user_lives == 0:
        print(f"You lose, the word was {chosen_word}")
        game_on = False

    # Winning condition
    elif "_" not in display:
        print("You win")
        game_on = False
