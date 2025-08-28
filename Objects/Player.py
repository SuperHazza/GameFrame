from GameFrame import RoomObject
import pygame

class Player(RoomObject):
    """
    A class for the player's avatar (the Player)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Player object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Player_frames\Player.png")
        self.set_image(image,64,64)

        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y_speed = -10
        elif key[pygame.K_s]:
            self.y_speed = 10
        elif key[pygame.K_a]:
            self.x_speed = -10
        elif key[pygame.K_d]:
            self.x_speed = 10