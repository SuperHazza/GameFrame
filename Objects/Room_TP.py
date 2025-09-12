from GameFrame import RoomObject

class Room_TP(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Room-Portal_frames\Room_TP.png")
        self.set_image(image,256,256)