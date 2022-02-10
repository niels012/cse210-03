from operator import indexOf

class Player:
    """A person who plays the game.

    The responsibility of the Player is to obtain user input and compare it with the game's word.

    Attributes:
        user_guess= User's guess
        indeces= List of indices of the User's guessed letter in the game's word.
        guess_wrong= Counter of user's wrong guesses.
        word (Words): The game's word.
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self._user_guess=' '
        self.indices=[]
        self.guess_wrong=0
<<<<<<< HEAD
        self.word=Words().word_picker()
        
    
=======
        pass

>>>>>>> 10f4728bfe9c3a95d93d96b06087035af6217b95
    def get_input(self):
        """Gets user's input (a letter).

        Args:
            self (Player): an instance of Player.
        """
<<<<<<< HEAD
        self._user_guess=input("Guess the letter: ")
    
    def compare_guess(self):
=======
        self._user_guess=input("Guess a letter [a-z]: ")
        pass

    def compare_guess(self,game_word):
>>>>>>> 10f4728bfe9c3a95d93d96b06087035af6217b95
        """Check if user's input (self._user_guess) is inside the word provided by 
            the Words class (self.word)

        Args:
            self (Player): an instance of Player.
            game_word: a word provided by the game.
        """
        self.get_input()
        if self._user_guess in game_word:
            self.guess_right(game_word)
        else:
            self.wrong()
<<<<<<< HEAD
        
    def guess_right(self):
=======
        pass

    def guess_right(self,game_word):
>>>>>>> 10f4728bfe9c3a95d93d96b06087035af6217b95
        """Updates self.index with the word's indices where the user's chosen letter
            is in.

        Args:
            self (Player): an instance of Player.
            game_word: a word provided by the game.
        """
        word=game_word
        guess=self._user_guess
        indices=[]
        for i in range(len(word)):
            if word[i] == guess:
                indices.append(i)
        self.indices= indices
<<<<<<< HEAD
        print(self.indices)
        
=======
        pass

>>>>>>> 10f4728bfe9c3a95d93d96b06087035af6217b95
    def wrong(self):
        """Adds 1 to the self.guess_wrog counter

        Args:
            self (Player): an instance of Player.
        """
        self.guess_wrong+=1
    

