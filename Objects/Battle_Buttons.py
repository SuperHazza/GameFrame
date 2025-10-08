from GameFrame import RoomObject
import pygame

class Run(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Run_Button.png")
        self.set_image(image, 128, 64)

    def update(self):
        # Check events for clicks
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("run")
            
class Attack(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Battle\Attack_Button.png")
        self.set_image(image,128,64)

class Items(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Battle\Item_Button.png")
        self.set_image(image,128,64)

class Swap(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Battle\Swap_Button.png")
        self.set_image(image,128,64)