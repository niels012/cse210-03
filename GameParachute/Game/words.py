import random

class Words:
    def __init__(self):
        # self.is_playing = True
        self._word = ""
        self._num_letter = 0
        # self.guess_letter = ""
        # self.guess_wrong = 0
        # self.score = 0
    # def start(self):
    #     self.word_picker()
    #     while self.is_playing == True:
    #         self.output()
    #         self.compare_guess()
    def word_picker(self):
        words_list = ["ox","cat","bear", "horse", "cow", "deer","mouse","rabbit","carabao","kangaroo"]
        # words_list =["door","deer","drag","born","bark","crab","roll","mock","spray"]
        pos_num = random.randint(0,len(words_list)-1)
        picked_word = words_list[pos_num]
        self._word = picked_word 
        num_letter = len(self._word)
        self._num_letter = num_letter
        return self._word
    def prn(self):
        print(self._word)
    # def output(self):
    #     if self.score == 0:
    #         for i in range(self.num_letter):
    #             print("_" ,end=" ")
    #         print()
    #     else:
    #         for j in range(self.score):
    #             print(self.word[j], end=" ")
    #         for blank in range(self.num_letter - self.score):
    #             print("_", end=" ")
    #         print()

    # def get_input(self):
    #     letter = input("Guess the letter: ")
    #     self.guess_letter = letter
    # def compare_guess(self):
    #         self.get_input()
    #         if self.guess_letter == self.word[self.score]:
    #             self.score += 1
    #             if self.score == self.num_letter:
    #                 self.output()
    #                 self.is_playing = False
    #                 print("You Win !!")
    #         else:
    #             self.guess_wrong += 1
    #             if self.guess_wrong == 4:
    #                 print("Game Over !!")
    #                 self.is_playing = False
    #             else:
    #                 print(f"You have {self.guess_wrong} mistake")
    #                 pass

# words = Words()
# words.word_picker()