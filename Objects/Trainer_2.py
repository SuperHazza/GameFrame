from GameFrame import RoomObject

class Trainer_2(RoomObject):
    """
    A class for the game's 2nd trainer
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        print("Loading image for Trainer_2:", "Trainer_frames/Trainer_2.png")
        image_2 = self.load_image("Trainer_frames/Trainer_2.png")
        self.set_image(image_2,64,64)