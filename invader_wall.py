from invaders_constants import *
import arcade
from PIL import Image

class Wall:

    def __init__(self, pos):
        self.patron = [0, 0, 0, 1, 1, 1, 0, 0, 0,
                       0, 0, 1, 1, 1, 1, 1, 0, 0,
                       0, 1, 1, 1, 1, 1, 1, 1, 0,
                       1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 0, 1, 1, 1, 1,
                       1, 1, 1, 0, 0, 0, 1, 1, 1]
        self.size = 16
        image_data = [1 for pix in range(1,self.size*self.size)]
        image = Image.new('RGB', (16,16), (255,255,255))

        textura = arcade.Texture(name='hola', image=image)
        self.block_list = arcade.SpriteList()
        for index, elemento in enumerate(self.patron):
            if elemento == 1:
                y = index%9
                sprite = arcade.Sprite()
                sprite.center_x = (index*self.size)+self.size/2
                sprite.center_y = (y *self.size)+ self.size/2
                sprite.width = self.size
                sprite.height = self.size
                sprite.texture = textura
                self.block_list.append(sprite)
        for ele in self.block_list:
            print(ele.center_x)