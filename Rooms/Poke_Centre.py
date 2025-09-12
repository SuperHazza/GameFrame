from GameFrame import Level
from Objects.Player import Player

class Poke_Centre(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Background.png")

        # add objects
        self.add_room_object(Player(self, 400, 600))
