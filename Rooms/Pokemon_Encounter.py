from GameFrame import Level, Globals
from Objects.Pokemon import Pokemon, Opponent_HP
from Objects.Player import Big_Player
from Objects.Battle_Buttons import Attack, Run, Swap, Items

Opponent_HP == 60

class Pokemon_Encounter(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Battle_Background.png")

        # add objects
        self.add_room_object(Pokemon(self, 620, 30))
        self.add_room_object(Big_Player(self, 177, 400))
        self.add_room_object(Attack(self, 650, 500))
        self.add_room_object(Run(self, 864, 628))   
        self.add_room_object(Swap(self, 864, 500))
        self.add_room_object(Items(self, 650, 628))

        # add HUD items
        self.opponent_hp = Opponent_HP(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.opponent_hp)
