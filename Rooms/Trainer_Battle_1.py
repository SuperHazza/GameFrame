from GameFrame import Level
from Objects.Pokemon import Pokemon
from Objects.Battle_Buttons import Attack, Run, Swap, Items

class Trainer_Battle_1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Battle_Background.png")

        # add objects
        from Objects.Player import Big_Player
        self.add_room_object(Pokemon(self, 700, 50))
        self.add_room_object(Big_Player(self, 100, 300))
        self.add_room_object(Attack(self, 650, 500))
        self.add_room_object(Run(self, 864, 628))   
        self.add_room_object(Swap(self, 864, 500))
        self.add_room_object(Items(self, 650, 628))


