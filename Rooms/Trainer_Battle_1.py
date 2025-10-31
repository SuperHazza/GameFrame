from GameFrame import Level, Globals
from Objects.Pokemon import Mega_Victribell, Opponent_HP, Player_HP
from Objects.Battle_Buttons import Attack, Run, Feed, Catch
from Objects.Battle_Effects import Miss, Crit

class Trainer_Battle_1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        Globals.OPPONENT_HP = 80
        
        # set background image
        self.set_background_image("Rooms\Battle_Background.png")

        # add objects
        from Objects.Player import Big_Player
#        self.add_room_object(Miss(self, 50, 50))
#        self.add_room_object(Crit(self, 50, 50))
        self.add_room_object(Mega_Victribell(self, 620, 30))
        self.add_room_object(Big_Player(self, 177, 400))
        self.add_room_object(Attack(self, 650, 500))
        self.add_room_object(Run(self, 864, 628))   
        self.add_room_object(Catch(self, 864, 500))
        self.add_room_object(Feed(self, 650, 628))

        # add HUD items
        self.opponent_hp = Opponent_HP(self, 
                           Globals.SCREEN_WIDTH/2 - 80, 20, 
                           str(Globals.OPPONENT_HP))
        self.add_room_object(self.opponent_hp)

        self.player_hp = Player_HP(self, 
                           Globals.SCREEN_WIDTH/2 - 180, 650, 
                           str(Globals.PLAYER_HP))
        self.add_room_object(self.player_hp)

