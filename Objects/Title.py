from GameFrame import RoomObject
import pygame

class Title(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Title.png")
        self.set_image(image,100,100)

        # register for key events
        self.handle_key_events = True 

    def key_pressed(self, key):
        """
        If the key pressed is X the game will start
        """
        
        if key[pygame.K_x]:
            self.room.running = False