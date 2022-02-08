from GameParachute.construct_para import Parachute
from GameParachute.player_input import Player
from GameParachute.words import Words


class Director:
    
# A person who directs the game. 
    
 # The responsibility of a Director is to control the sequence of play."""

    def __init__ (self):

        self._parachute = Parachute()
        self._is_playing=True
        pass

    def start_game (self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        pass
    
    def _get_inputs(self):
        pass

    def _do_updates (self):
        pass
    def _do_outputs (self):
        pass