from GameFrame import RoomObject, Globals
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
            self.y -= 10
        elif key[pygame.K_s]:
            self.y += 10
        if key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10

    def keep_in_room(self):
        """
        Keeps the player inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        elif self.x < 0:
            self.x = 0
        elif self.x + self.width> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def step(self):
        """
        Determine what happens to the Player on each click of the game clock
        """
        self.keep_in_room()