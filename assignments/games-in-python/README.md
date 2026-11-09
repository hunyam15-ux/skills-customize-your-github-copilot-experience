# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game to practice Python strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Hidden Word

#### Description
Create the game setup that selects a secret word from a predefined list and tracks the player's progress and guesses.

#### Requirements
Completed program should:

- Select one word at random from a predefined list.
- Display the secret word as underscores, with one underscore for each letter.
- Track the letters the player has guessed and the number of incorrect guesses remaining.

### 🛠️ Run the Guessing Game

#### Description
Build the game loop so the player can guess letters, reveal matching letters, and finish the game by guessing the word or running out of attempts.

#### Requirements
Completed program should:

- Prompt the player to enter a letter and reveal every matching position in the secret word.
- Reduce the remaining incorrect guesses when the letter is not in the secret word.
- Continue displaying the word's progress and remaining incorrect guesses after each guess.
- End when the player reveals the whole word or has no incorrect guesses remaining.
- Display a clear win message when the player guesses the word and a lose message when attempts run out.
