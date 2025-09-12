from GameFrame import Level
from Objects.Trainer_1 import Trainer_1
from Objects.Trainer_2 import Trainer_2
from Objects.Grass import Grass
from Objects.Room_TP_2 import Room_TP_2

class GamePlay_2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Background.png")

        # add objects
        from Objects.Player import Player
        self.add_room_object(Player(self, 25, 50))
        self.add_room_object(Trainer_1(self,200, 600))
        self.add_room_object(Trainer_2(self,600, 100))
        self.add_room_object(Grass(self,500, 400))
        self.add_room_object(Room_TP_2(self,50, 200))
