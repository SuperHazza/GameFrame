from GameFrame import Level
from Objects.Player import Player
from Objects.Trainer_1 import Trainer_1
from Objects.Trainer_2 import Trainer_2
from Objects.Grass import Grass

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Background.png")

        # add objects
        self.add_room_object(Player(self, 25, 50))
        self.add_room_object(Trainer_1(self,400, 600))
        self.add_room_object(Trainer_2(self,800, 100))
        self.add_room_object(Grass(self,600, 500))
