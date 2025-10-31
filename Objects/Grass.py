from GameFrame import RoomObject

class Grass(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Encounter-Zones_frames\Grass.png")
        self.set_image(image,256,256)

class Desert_Grass(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Encounter-Zones_frames\Desert_Grass.png")
        self.set_image(image,256,256)

class Icy_Water(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Encounter-Zones_frames\Icy_Water.png")
        self.set_image(image,256,256)