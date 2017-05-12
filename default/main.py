from default.hangman import Hangman


def main():
    # Create Hangman game
    game = Hangman("words.txt")
    # Welcome Message for user
    print """Welcome, user, to the exciting game that is Hangman!
We have randomly selected a word from a text file for you to try and guess.
Good luck and have fun!"""
    # Begin Game Loop
    game.game_loop()


# Call to main method
main()
