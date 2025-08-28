from GameFrame import RoomObject

class Trainer_2(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Trainer_frames\Trainer_2.png")
        self.set_image(image,64,64)