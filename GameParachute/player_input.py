from operator import indexOf
from words import Words

class Player:
    def __init__(self):
        self._user_guess=' '
        self.index=0
        self.guess_wrong=0
        self.word=Words().word_picker()
        
        pass
    def get_input(self):
        # letter = input("Guess the letter: ")
        self._user_guess=input("Guess the letter: ")
        pass
    def compare_guess(self):
        # self.func.word_picker()
        self.get_input()
        if self._user_guess in self.word:
            self.guess_right()
        else:
            self.wrong()
        pass
    def guess_right(self):
        # self.func.word_picker()
        word=self.word
        guess=self._user_guess
        self.index= indexOf(word,guess)
        self.word[self.index]=self._user_guess
        pass
    def wrong(self):
        self.guess_wrong+=1
        pass

Player().compare_guess()