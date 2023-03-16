
## Problem
Design and implement hangman game.

## Requirements
### Q. What is the objective of the game ?  
A. The objective of the game is to guess a word by guessing its letters by within limited number of tries. Player wins if the word is guessed with limited number of tries, else loses

### Q. How will the game start ?  
A. The game starts by displaying the number of letters to be guessed and number of retries left for the player to try. It will also show the letters already guessed

### Q: How will the player input their guesses ?
A: Player will guess one letter at timea and get it validated

### Q: How will the players input be validated ?
A: The game will check if the letter guessed by user is in the word. if the letter is there then the game will update the display with found word.
If not it will decrement the available retry count

### Q: How will the game end?
A: The game end when the player has either guessed all the words or if the number of retries for the user have finished.

### Q: How will the game validate the user's input ?
A: The game will check if display message incase of a guessed letter and alert user for any other warnings.