import arcade
from player import Player
from invaders_constants import *
from invader_wall import Wall

class Invaders(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None
        self.wall = Wall(50, 5)
        # Separate variable that holds the player sprite
        self.player_sprite = None
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # self.physics_engine = None
        self.keys_pressed_status = {}

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.laser_list = arcade.SpriteList()


        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = Player(0, 0, self.laser_list)
        self.player_list.append(self.player_sprite)

        # # Create the ground
        # # This shows using a loop to place multiple sprites horizontally
        # for x in range(0, 1250, 64):
        wall = arcade.Sprite()
        wall.width = 1
        wall.height = 650
        wall.center_x = 1
        wall.center_y = 650/2
        self.wall_list.append(wall)

        wall = arcade.Sprite()
        wall.width = 1
        wall.height = 650
        wall.center_x = 1000
        wall.center_y = 650 / 2
        self.wall_list.append(wall)

        self.keys_pressed_status[arcade.key.SPACE] = False
        self.keys_pressed_status[arcade.key.LEFT] = False
        self.keys_pressed_status[arcade.key.RIGHT] = False


        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        # coordinate_list = [[512, 96], [256, 96], [768, 96]]

        # for coordinate in coordinate_list:
        #     # Add a crate on the ground
        #     wall = arcade.Sprite(
        #         ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
        #     )
        #     wall.position = coordinate
        #     self.wall_list.append(wall)
        # Create the 'physics engine'
        # self.physics_engine = arcade.PhysicsEngineSimple(
        #     self.player_sprite, self.wall_list)

    def on_update(self, delta_time):
        """Movement and game logic"""
        # Move the player with the physics engine
        # self.physics_engine.update()
        self.player_list.update()
        self.laser_list.update()


    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here
        self.player_list.draw()
        self.laser_list.draw()
        self.wall.block_list.draw()



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        self.keys_pressed_status[key] = True
        self.player_sprite.get_input(self.keys_pressed_status)


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        self.keys_pressed_status[key] = False
        self.player_sprite.get_input(self.keys_pressed_status)



def main():
    """Main function"""
    window = Invaders()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()