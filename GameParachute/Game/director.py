from game.construct_para import Parachute
from game.player_input import Player
from game.words import Words


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
       

    def start_game (self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
       
    
    def _get_inputs(self):
        """ gets player input for the parachute"""
        guess = self._game.update_parachute ("\nGuess the letter: ")
        self._parachute.display_parachute (guess)
        

    def _do_updates (self):
        """Keeps track of the parachute

        Args:
            self (Director): An instance of Director.
        """
        self._Player.compare_guess(self._parachute)
        
    def _do_outputs (self):
         """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        