from GameFrame import RoomObject
import pygame

class Run(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Run_Button.png")
        self.set_image(image, 128, 64)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 864 <= mouse_x <= 992 and 628 <= mouse_y <= 692:
                print("Run from battle")
        

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