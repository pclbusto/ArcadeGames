
import arcade
from invaders_constants import *

class Laser(arcade.Sprite):
    IMAGE_PATH = "sprites/invaders_sprites_laser.png"
    def __init__(self, pos, speed):
        super(Laser, self).__init__(Laser.IMAGE_PATH)
        self.speed = speed
        self.center_x = pos[0]
        self.center_y = pos[1]
        self.change_y = speed

    def get_input(self, key, modifiers):
        pass

    def update(self):
        self.center_y += self.change_y
        if self.bottom > SCREEN_HEIGHT:
            self.kill()
