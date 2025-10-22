from GameFrame import Level
from Objects.Store_Buttons import Buy_1, Buy_2, Exit, Item_1, Item_2

class Poke_Store(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Store_Background.png")

        # add objects
        self.add_room_object(Buy_1(self, 500, 200))
        self.add_room_object(Buy_2(self, 500, 378))
        self.add_room_object(Exit(self, 500, 556))
        self.add_room_object(Item_1(self, 200, 200))
        self.add_room_object(Item_2(self, 200, 378))

    
