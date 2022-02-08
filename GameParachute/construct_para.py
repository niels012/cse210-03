class Parachute:

    # Setting the initial value

    def __init__(self):
        self._parachute = ["  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"]
    
    # Updating the parachute output according to the answers

    def update_parachute (self):
        if self.guess_wrong == 0:
            self._parachute = ["  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"]
        elif self.guess_wrong == 1:
            self._parachute = [" /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"]
        elif self.guess_wrong == 2:
            self._parachute = [" \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"]
        elif self.guess_wrong == 3:
            self._parachute = ["  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"]
        else:
            self._parachute = ["   x \n  /|\ \n  / \ \n \n^^^^^^^"]

    # Displaying the updated parachute
        
    def display_parachute (self):
        print(self._parachute)

### Note! ###

#   The "self.guess_wrong" above doesn't need to be that name. Whoever's responsible for counting answers can choose the name they want.


    
# complete
# ("  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^")
# one wrong
# (" /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^")
# two wrong
# (" \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^")
# last chance 
# ("  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^")
# game over
# ("   x \n  /|\ \n  / \ \n \n^^^^^^^")

    
