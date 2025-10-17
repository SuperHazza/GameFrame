from GameFrame import RoomObject, Globals
import pygame


class Miss(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Miss.png")
        self.set_image(image, 128, 64)

class Crit(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Crit.png")
        self.set_image(image, 128, 64)