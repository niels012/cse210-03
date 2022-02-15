import random

class Words:
    """
    The word provided by the game.

    The responsability of Words is to pick a random word from a list and use it for the game.

    Attributes:
        word: The game's word.
        
    """

    def __init__(self):
        """Constructs a new Words
        
        Args:
            self (Words): an instance of Player.
        """
        self.word = ""


    def word_picker(self):
        """
        Takes a random word from a list of words.
        
        Args:
            self (Words): an instance of Words.
        """
        words_list = ["ox","cat","deer","mouse","rabbit","carabao","kangaroo"]
        # words_list =["door","deer","drag","born","bark","crab","roll","mock","spray"]
        pos_num = random.randint(0,len(words_list)-1)
        picked_word = words_list[pos_num]
        self.word = picked_word
        return self.word


