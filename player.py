
import arcade

class Player(arcade.Sprite):
    IMAGE_PATH = "sprites/invaders_sprites_player.png"
    PLAYER_MOVEMENT_SPEED = 5

    def __init__(self, pos, speed):
        super(Player, self).__init__(Player.IMAGE_PATH)
        self.speed = speed
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.center_x = 52 / 2
        self.center_y = 32 / 2

    def get_input(self, keys_pressed_status):
        if keys_pressed_status[arcade.key.LEFT]:
            self.change_x = -Player.PLAYER_MOVEMENT_SPEED
        if keys_pressed_status[arcade.key.RIGHT]:
            self.change_x = Player.PLAYER_MOVEMENT_SPEED
        if not keys_pressed_status[arcade.key.RIGHT] and not keys_pressed_status[arcade.key.LEFT] :
            self.change_x = 0
        if keys_pressed_status[arcade.key.SPACE]:
            self.shoot_laser()


    def shoot_laser(self):
        print("shoot laser")