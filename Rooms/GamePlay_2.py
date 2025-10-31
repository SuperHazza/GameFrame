from GameFrame import Level
from Objects.Trainer_1 import Trainer_1
from Objects.Trainer_2 import Trainer_2
from Objects.Grass import Icy_Water
from Objects.Room_TP import Room_TP_3, Room_TP_4
from Objects.Poke_Store import Poke_Store

class GamePlay_2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Ice_Cave_Background.png")

        # add objects
        from Objects.Player import Player
        self.add_room_object(Player(self, 300, 300))
        self.add_room_object(Icy_Water(self,200, 500))
        self.add_room_object(Room_TP_4(self, 800, 300))
        self.add_room_object(Room_TP_3(self,25, 300))

