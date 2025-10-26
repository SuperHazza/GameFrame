from GameFrame import Level
from Objects.Catch_Buttons import Yes_Button, No_Button, Replace_Text

class Catch_Room(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Catch_Background.png")

        # add objects
        self.add_room_object(Yes_Button(self, 347, 500))
        self.add_room_object(No_Button(self,549, 500))
        self.add_room_object(Replace_Text(self,400, 100))