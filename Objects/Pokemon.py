from GameFrame import RoomObject, TextObject, Globals

class Pokemon(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Pokemon_frames\Pokemon.png")
        self.set_image(image,256,256)

class Opponent_HP(TextObject):

    def __init__(self, room, x: int, y: int, text=None):
      
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()

    def update_opponent_hp(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.OPPONENT_HP += change
        self.text = str(Globals.OPPONENT_HP)
        self.update_text()

class Player_HP(TextObject):

    def __init__(self, room, x: int, y: int, text=None):
      
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        
    def update_player_hp(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.PLAYER_HP += change
        self.text = str(Globals.PLAYER_HP)
        self.update_text()