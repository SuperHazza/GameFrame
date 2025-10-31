from GameFrame import RoomObject

class Room_TP(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Room-Portal_frames\Room_TP.png")
        self.set_image(image,256,256)

class Room_TP_3(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Room-Portal_frames\Room_TP_3.png")
        self.set_image(image,256,256)

class Room_TP_4(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Room-Portal_frames\Room_TP_4.png")
        self.set_image(image,256,256)