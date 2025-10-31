from GameFrame import Level
from Objects.Trainer_1 import Trainer_1
from Objects.Trainer_2 import Trainer_2
from Objects.Grass import Desert_Grass
from Objects.Room_TP_2 import Room_TP_2
from Objects.Poke_Store import Poke_Store

class GamePlay_3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Desert_Background.png")

        # add objects
        from Objects.Player import Player
        self.add_room_object(Player(self, 300, 300))
        self.add_room_object(Trainer_1(self,465, 50))
        self.add_room_object(Trainer_2(self,650, 640))
        self.add_room_object(Desert_Grass(self,750, 500))
        self.add_room_object(Room_TP_2(self,25, 200))
        self.add_room_object(Poke_Store(self,845, 300))