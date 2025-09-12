from GameFrame import RoomObject

class Poke_Centre(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Poke-Centre_frames\Poke_Centre.png")
        self.set_image(image,128,128)