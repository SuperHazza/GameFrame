from GameFrame import RoomObject, Globals
import pygame

class Yes_Button(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Catch-Room_frames/Yes_Button.png")
        self.set_image(image, 128, 64)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 347 <= mouse_x <= 347+128 and 500 <= mouse_y <= 564:
                print("You chose to catch the Pokemon")
                Globals.MYSTERY_MEAT_STOCK += 1
                Globals.CURRENT_POKEMON = Globals.Last_Opponent_Pokemon
                Globals.next_level = Globals.levels.index("GamePlay")
                self.room.running = False


class No_Button(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Catch-Room_frames/No_Button.png")
        self.set_image(image, 128, 64)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 549 <= mouse_x <= 549+128 and 500 <= mouse_y <= 564:
                print("You chose not to catch the Pokemon")
                Globals.MYSTERY_MEAT_STOCK += 1
                Globals.next_level = Globals.levels.index("GamePlay")
                self.room.running = False

class Replace_Text(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Catch-Room_frames/Replace_Text.png")
        self.set_image(image, 256, 256)
                