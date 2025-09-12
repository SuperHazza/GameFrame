from GameFrame import Level
from Objects.Pokemon import Pokemon

class Trainer_Battle_1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Background.png")

        # add objects
        from Objects.Player import Big_Player
        self.add_room_object(Pokemon(self, 700, 50))
        self.add_room_object(Big_Player(self, 100, 300))

