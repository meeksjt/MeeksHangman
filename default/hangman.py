from default.hangmanfigure import HangmanFigure
from random import randint


class Hangman(object):
    """Class to represent Hangman Game"""
    guess_num = 0               # Number of Current Guesses
    guessed_letters = []        # Letters Guessed
    word_guess = ""             # Word Guess

    def __init__(self, file_name):
        self.hangman_word = self.get_word(file_name)        # Assign random hangman word from file
        self.word_guess = "_" * len(self.hangman_word)      # Creates blank spaces for word guess
        self.hangman_figure = HangmanFigure()               # creates new Hangman Figure for display

    def get_word(self, file_name):
        """Read potential Hangman words into a list, remove whitespace and newlines and such"""
        with open(file_name, "r") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        # Get the word for the Hangman game and create a new game
        word = content[randint(0, len(content) - 1)]
        return word

    def check_letter_guess(self, char):
        """
        Check to see if the user's guess is in the word
        Also sets the current user guess to the new guess
        """
        char_in_word = False
        new_word_guess = []
        # Compare the letters in the word to the guess character
        for i in range(len(self.hangman_word)):
            if self.hangman_word[i] == char:
                char_in_word = True
                new_word_guess.append(char)
            else:
                new_word_guess.append(self.word_guess[i])
        self.word_guess = "".join(new_word_guess)
        return char_in_word

    def game_loop(self):
        while self.guess_num <= 5:
            self.hangman_figure.print_current_hangman()
            self.print_current_word_guess()
            self.print_letters_guessed()

            letter_guess = raw_input("Enter a letter that has not already been guessed: ")
            while letter_guess in self.guessed_letters or not letter_guess.isalpha() or len(letter_guess) != 1:
                if letter_guess in self.guessed_letters:
                    letter_guess = raw_input("That letter has already been guessed.  Try again! ")
                elif not letter_guess.isalpha():
                    letter_guess = raw_input("That is not a letter! Try again! ")
                elif len(letter_guess) != 1:
                    letter_guess = raw_input("Please enter a single alphabetic character! ")
                break

            self.guessed_letters.append(letter_guess)
            letter_in_the_word = self.check_letter_guess(letter_guess)
            if letter_in_the_word:
                print "Great guess: %s is in the word!" % letter_guess
            else:
                print "Too bad! %s is not in the word!" % letter_guess
                self.guess_num += 1
                self.hangman_figure.update_figure(self.guess_num)

            if self.word_guess == self.hangman_word:
                print "Congratulations!  You won!"
                break
        else:
            print "Aww, too bad!  Better luck next time!"

    def print_letters_guessed(self):
        print "Letters Guessed: ",
        for i in self.guessed_letters:
            print i,
        print

    def print_current_word_guess(self):
        for i in range(len(self.word_guess)):
            print str(self.word_guess[i]) + " ",
        print
        print
