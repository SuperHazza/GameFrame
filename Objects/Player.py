from GameFrame import RoomObject, Globals
from Rooms import Trainer_Battle_1, GamePlay_2
from Objects.Pokemon import Opponent_HP, Player_HP
import pygame
import time
import random

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

        # register events
        self.register_collision_object("Trainer_1")
        self.register_collision_object("Trainer_2")
        self.register_collision_object("Grass")
        self.register_collision_object("Room_TP")
        self.register_collision_object("Room_TP_2")
        self.register_collision_object("Poke_Centre")
        self.register_collision_object("Poke_Store")
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y -= 5
        elif key[pygame.K_s]:
            self.y += 5
        if key[pygame.K_a]:
            self.x -= 5
        elif key[pygame.K_d]:
            self.x += 5
        elif key[pygame.K_UP]:
            self.image.set_alpha(10)
        elif key[pygame.K_DOWN]:
            self.image.set_alpha(255)

    def keep_in_room(self):
        """
        Keeps the player inside the room
        """
        if self.y < 100:
            self.y = 100
        elif self.y + self.height> Globals.SCREEN_HEIGHT-100:
            self.y = Globals.SCREEN_HEIGHT-100 - self.height
        elif self.x < 0:
            self.x = 0
        elif self.x + self.width> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def step(self):
        """
        Determine what happens to the Player on each click of the game clock
        """
        self.keep_in_room()

    def handle_collision(self, other, other_type):

        if other_type == "Trainer_1":
            # Find the index of Trainer_Battle_1 in Globals.levels
            if "Trainer_Battle_1" in Globals.levels:
                Globals.next_level = Globals.levels.index("Trainer_Battle_1")
            self.room.running = False

        if other_type == "Trainer_2":
            # Find the index of Trainer_Battle_2 in Globals.levels
            if "Trainer_Battle_2" in Globals.levels:
                Globals.next_level = Globals.levels.index("Trainer_Battle_2")
            self.room.running = False

        if other_type == "Room_TP":
            print("Teleported!")
            if "GamePlay_2" in Globals.levels:
                Globals.next_level = Globals.levels.index("GamePlay_2")
            self.room.running = False

        if other_type == "Room_TP_2":
            print("Teleported!")
            if "GamePlay" in Globals.levels:
                Globals.next_level = Globals.levels.index("GamePlay")
            self.room.running = False

        if other_type == "Poke_Store":
            print("Store Entered!")
            if "Poke_Store" in Globals.levels:
                Globals.next_level = Globals.levels.index("Poke_Store")
                print("hiiiii")
            self.room.running = False

        if other_type == "Poke_Centre":
            print("Healed at Poke Centre!")
            Globals.PLAYER_HP = 60

            # When player steps into grass
        if other_type == "Grass":
            if not hasattr(self, "in_grass") or not self.in_grass:  # only trigger when first stepping in
                self.in_grass = True
                print("Stepped in Grass!")

                # Set a future time for the encounter
                self.encounter_time = time.time() + random.randint(1, 5)
                self.encounter_triggered = False

        # Somewhere in your game loop, keep checking:
        if hasattr(self, "in_grass") and self.in_grass and not self.encounter_triggered:
            if time.time() >= self.encounter_time:  # Time has passed
                print("POKEMON ENCOUNTER!!!!!")

                if "Pokemon_Encounter" in Globals.levels:
                    Globals.next_level = Globals.levels.index("Pokemon_Encounter")
                    self.room.running = False

                self.encounter_triggered = True  # so it doesn't trigger repeatedly

        # When player leaves the grass
        if other_type != "Grass":
            self.in_grass = False
            self.encounter_time = 0
            self.encounter_triggered = False

class Big_Player(RoomObject):

    def __init__(self, room, x, y):
        
        RoomObject.__init__(self, room, x, y)
        
        # set image
        if Globals.CURRENT_POKEMON == "Pikachu":
            image = self.load_image("Pokemon_frames\Pikachu.png")
            self.set_image(image,256,256)
        elif Globals.CURRENT_POKEMON == "Alolan_Diglet":
            image = self.load_image("Pokemon_frames\Alolan_Diglet.png")
            self.set_image(image,256,256)
        elif Globals.CURRENT_POKEMON == "Hisuian_Zorua":
            image = self.load_image("Pokemon_frames\Hisuian_Zorua.png")
            self.set_image(image,256,256)
        elif Globals.CURRENT_POKEMON == "Pancham":
            image = self.load_image("Pokemon_frames\Pancham.png")
            self.set_image(image,256,256)
        elif Globals.CURRENT_POKEMON == "Mega_Victribell":
            image = self.load_image("Pokemon_frames\Mega_Victribell.png")
            self.set_image(image,256,256)