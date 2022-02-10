from Game.construct_para import Parachute
from Game.player_input import Player
from Game.words import Words


class Director:
    
# A person who directs the game. 
    
 # The responsibility of a Director is to control the sequence of play."""

    def __init__ (self):
        
        """Constructs a new Director. 
        Args:
        Director (self) An instance of director"""
        self._parachute = Parachute()
        self._is_playing=True
        self.player_input = Player()
        self.words = Words()
        self.game_word=self.words.word_picker()
        self.indices=self.player_input.indices
       

    def start_game (self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # To start we print the parachute.
        self._parachute.display_parachute()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
       
    
    def _get_inputs(self):
        """ gets player input for the parachute
        
        Args:
            self (Director): An instance of Director.        
        """

        self.player_input.compare_guess(self.game_word)
        

    def _do_updates (self):
        """Keeps track of the parachute

        Args:
            self (Director): An instance of Director.
        """
        guess_wrong=self.player_input.guess_wrong
        self.indices=self.player_input.indices
        self._parachute.update_parachute(guess_wrong,self.game_word,self.player_input._user_guess,self.indices)
        

    def _do_outputs (self):
         """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
         self._parachute.display_parachute()
         if '_' in self._parachute._word_space:
             self._is_playing=True
         else:
             print('You won!')
             self._is_playing=False
         if self._parachute._parachute=="   x \n  /|\ \n  / \ \n \n^^^^^^^":
             print('You lost :( Good luck next time (;')
             self._is_playing=False
