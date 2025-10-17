from GameFrame import RoomObject, Globals
import pygame
from Objects.Pokemon import Opponent_HP, Player_HP
import time
import random

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
                Globals.next_level = Globals.levels.index("GamePlay")
                self.room.running = False    

class Attack(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Attack_Button.png")
        self.set_image(image, 128, 64)
        
        self.handle_key_events = True
        self.previous_mouse = None

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0] and self.previous_mouse != pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 650 <= mouse_x <= 778 and 500 <= mouse_y <= 564:
                miss_crit_2 = random.randint(1, 20)
                print(miss_crit_2)
                if miss_crit_2 == 2:
                    print("Your attack missed!")
                elif miss_crit_2 == 3:
                    self.room.opponent_hp.update_opponent_hp(random.randint(-24, -16))
                    print("You hit a critical hit!")
                else:
                    self.room.opponent_hp.update_opponent_hp(random.randint(-12, -8))
                    print("You Attacked the Opponent")
                self.set_timer(30, self.enemy_attack)
        self.previous_mouse = pygame.mouse.get_pressed()[0]

    def enemy_attack(self):
        if Globals.OPPONENT_HP <= 0:
            print("Opponent Defeated")
            Globals.next_level = Globals.levels.index("GamePlay")
            self.room.running = False
        else:
            miss_crit = random.randint(1, 20)
            print(miss_crit)
            if miss_crit == 2:
                print("The opponent's attack missed!")
            elif miss_crit == 3:
                self.room.player_hp.update_player_hp(random.randint(-20, -12))
                print("The Opponent Hit a Critical Hit!")
                if Globals.PLAYER_HP <= 0:
                    print("You have been defeated!")
                    Globals.next_level = Globals.levels.index("GamePlay")
                    self.room.running = False
            else:
                self.room.player_hp.update_player_hp(random.randint(-10, -6))
                print("You got attacked")
                if Globals.PLAYER_HP <= 0:
                    print("You have been defeated!")
                    Globals.next_level = Globals.levels.index("GamePlay")
                    self.room.running = False
        
                

class Items(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Item_Button.png")
        self.set_image(image, 128, 64)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 650 <= mouse_x <= 778 and 628 <= mouse_y <= 692:
                print("Accessed Items")

class Swap(RoomObject):

    def __init__(self, room, x, y):
        super().__init__(room, x, y)
        image = self.load_image("Battle/Swap_Button.png")
        self.set_image(image, 128, 64)
        
        self.handle_key_events = True

    def key_pressed(self, key):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 864 <= mouse_x <= 992 and 500 <= mouse_y <= 564:
                print("Swapped Pokemon")