
import arcade
from laser import Laser
from invaders_constants import *

class Player(arcade.Sprite):
    IMAGE_PATH = "sprites/invaders_sprites_player.png"
    PLAYER_MOVEMENT_SPEED = 5

    def __init__(self, pos, speed, laser_list):
        super(Player, self).__init__(Player.IMAGE_PATH)
        self.speed = speed
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 60
        self.center_x = 52 / 2
        self.center_y = 32 / 2
        self.laser_list = laser_list
        self.ready = True

    def get_input(self, keys_pressed_status):
        if keys_pressed_status[arcade.key.LEFT]:
            self.change_x = -Player.PLAYER_MOVEMENT_SPEED
        if keys_pressed_status[arcade.key.RIGHT]:
            self.change_x = Player.PLAYER_MOVEMENT_SPEED
        if not keys_pressed_status[arcade.key.RIGHT] and not keys_pressed_status[arcade.key.LEFT] :
            self.change_x = 0
        if keys_pressed_status[arcade.key.SPACE]:
            self.shoot_laser()

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        self.laser_time += 1
        if self.laser_time > self.laser_cooldown:
            self.ready = True
            self.laser_time = 0

    def shoot_laser(self):
        if self.ready:
            pos = (self.center_x, self.center_y)
            laser = Laser(pos, 8)
            self.laser_list.append(laser)
            self.ready = False
