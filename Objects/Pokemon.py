from GameFrame import RoomObject

class Pokemon(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Pokemon_frames\Pokemon.png")
        self.set_image(image,256,256)