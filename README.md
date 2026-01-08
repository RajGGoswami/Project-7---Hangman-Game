# Project-7---Hangman-Game

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to build a fully playable Hangman game where the user guesses letters to uncover a hidden word.

**Project Overview**

This project is a text-based implementation of the classic Hangman game.

The game includes:

A randomly selected word

A limited number of lives

Visual stages showing progress

User feedback for correct and incorrect guesses

The program then:

Loops continuously until the game is won or lost

Updates the displayed word as letters are guessed

Reduces lives for incorrect guesses

Ends when the player wins or runs out of lives

**Project File Structure**

The project is organised into multiple files to separate logic, data, and visual assets.

main.py
Contains the main game logic and user interaction loop.

art.py
Stores ASCII art including the logo, welcome message, and hangman stages.

hangman_words.py
Contains the list of possible words used by the game.

**Why this project exists**

This project represents a major step in combining multiple concepts into one cohesive program.

It allowed me to:

Manage game state across multiple turns

Track progress dynamically

Handle user interaction inside a loop

Combine logic, loops, and conditionals into a complete game

**What I learned**

How to use while loops to control game flow

How to work with lists and strings together

How to iterate using indexes to update values

How to track and update remaining lives

How to implement win and lose conditions

How to import and use external modules and assets

**How the code works (step-by-step)**

Select a random word from a predefined list

Replace each letter with an underscore placeholder

Repeat until the game ends

Ask the user to guess a letter

Check if the guess is correct, incorrect, or repeated

Update the display and remaining lives

End the game when the word is guessed or lives reach zero

**Example Output**

Welcome to Hangman

Guess a letter: a

_ a _ _ _

You have 6 lives left

Guess a letter: z

You guessed z, that's not in the word. You lose a life
