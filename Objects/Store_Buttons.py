from GameFrame import RoomObject, Globals
import pygame
import time
import random

class Item_1(RoomObject):
    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Poke-Store_frames/Item_1.png")
        self.set_image(image, 256, 128)

class Item_2(RoomObject):
    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Poke-Store_frames/Item_2.png")
        self.set_image(image, 256, 128)

class Buy_1(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Poke-Store_frames/Buy_1.png")
        self.set_image(image, 256, 128)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 500 <= mouse_x <= 756 and 200 <= mouse_y <= 328:
                print("bought an item 1")
                Globals.POKE_BALLS += 1
                print("You now have", Globals.POKE_BALLS, "Poke Balls!")

class Buy_2(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Poke-Store_frames/Buy_2.png")
        self.set_image(image, 256, 128)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 500 <= mouse_x <= 756 and 378 <= mouse_y <= 506:
                print("bought an item 2")
                Globals.MYSTERY_MEAT += 1
                print("You now have", Globals.MYSTERY_MEAT, "Mystery Meats!")

class Exit(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Poke-Store_frames/Exit_Button.png")
        self.set_image(image, 256, 128)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 500 <= mouse_x <= 756 and 556 <= mouse_y <= 682:
                print("Exiting Poke Store")
                Globals.next_level = Globals.levels.index("GamePlay_2")
                self.room.running = False