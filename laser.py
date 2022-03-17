
import arcade

class Laser(arcade.Sprite):
    IMAGE_PATH = "sprites/invaders_sprites_laser.png"
    def __init__(self, pos, speed):
        super(Laser, self).__init__(Laser.IMAGE_PATH)
        self.speed = speed
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

    def get_input(self, key, modifiers):
        pass

    def shoot_laser(self):
        print("shoot laser")