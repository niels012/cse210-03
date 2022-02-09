from operator import indexOf
from words import Words

class Player:
    """A person who plays the game.

    The responsibility of the Player is to obtain user input and compare it with the game's word.

    Attributes:
        user_guess= User's guess
        index= Index of the User's guessed letter in the game's word.
        guess_wrong= Counter of user's wrong guesses.
        word (Words): The game's word.
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self._user_guess=' '
        self.index=0
        self.guess_wrong=0
        self.word=Words().word_picker()
        
        pass
    def get_input(self):
        """Gets user's input (a letter).

        Args:
            self (Player): an instance of Player.
        """
        self._user_guess=input("Guess the letter: ")
        pass
    def compare_guess(self):
        """Check if user's input (self._user_guess) is inside the word provided by 
            the Words class (self.word)

        Args:
            self (Player): an instance of Player.
        """
        self.get_input()
        if self._user_guess in self.word:
            self.guess_right()
        else:
            self.wrong()
        pass
    def guess_right(self):
        """Updates self.index with the word's index where the user's chosen letter
            is in.

        Args:
            self (Player): an instance of Player.
        """
        word=self.word
        guess=self._user_guess
        self.index= indexOf(word,guess)
        pass
    def wrong(self):
        """Adds 1 to the self.guess_wrog counter

        Args:
            self (Player): an instance of Player.
        """
        self.guess_wrong+=1
        pass


#This last line was just to test the class. Erase when the program is finished
# Player().compare_guess()