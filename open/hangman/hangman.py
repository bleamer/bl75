# Desing and implement hangman game

import random

class Hangman():
    def __init__(self, word_list, retries = 6):
        self.word_list = word_list
        self.retries_left = retries
        self.word = self.__get_random_word().lower()
        self.guessed = []
        self.last_message = ''
        self.word_progress = ['_' for i in range(len(self.word))]

    def __get_random_word(self):
        return random.choice(self.word_list)

        

    def make_guess(self, c):
        c = c.lower()
        if c in self.guessed:
            return False
        if c in self.word:
            for i in range(len(self.word)):
                if self.word[i] == c:
                    self.word_progress[i] = c
        else:
            self.retries_left -= 1
        
        self.guessed.append(c)
        return True
        

    def is_game_over(self):
        if self.retries_left == 0:
            return True
        if "_" not in self.word_progress:
            return True
        return False
    
    def print_word_progress(self):
        print("Word prgress: "+" ".join(self.word_progress)+"\n")

    def print_guesses_left(self):
        print(f"Guesses left: {self.retries_left}\n")
    
    def print_guesses(self):
        print(f"Guesses done: {' '.join(self.guessed)}")

    def print_game_state(self):
        print('-'*15+' Hangman '+'-'*15)
        self.print_word_progress()
        self.print_guesses_left()
        self.print_guesses()
        print("-"*35+'\n')




if __name__ == "__main__":
    wordlist = ['hello', 'world', 'python', 'google','apple', 'amazon']
    hangman = Hangman(wordlist)

    while not hangman.is_game_over():
        hangman.print_game_state()
        guess = input("Guess a letter: ")
        hangman.make_guess(guess)

    hangman.print_game_state()

    if "_" in hangman.word_progress:
        print(f'You lose, the word was: {hangman.word}', )
    else:
        print("You win!\n\n")