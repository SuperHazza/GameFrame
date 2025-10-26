from GameFrame import Level

class Poke_Store(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Rooms\Catch_Background.png")

        # add objects