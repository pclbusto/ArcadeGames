from invaders_constants import *
import arcade
from PIL import Image
from copy import copy

class Wall:

    def __init__(self, pos, quantity=1):
        self.patron = [
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                       ]
        self.patron.reverse()
        self.size = 4
        self.quantity = quantity
        self.width = len(self.patron[0])
        image = Image.new('RGB', (self.size, self.size), (255, 255, 255))
        #lista para guardar 1 conjunto de bloques que construyen el patron
        self.list_blocks = []
        textura = arcade.Texture(name='hola', image=image)
        for index_y, lista in enumerate(self.patron):
            y = index_y
            for index_x, elemento in enumerate(lista):
                x = index_x
                if elemento == 1:
                    sprite = arcade.Sprite()
                    sprite.center_x = (x*self.size)+self.size/2
                    sprite.center_y = (y*self.size)+self.size/2
                    sprite.width = self.size
                    sprite.height = self.size
                    sprite.texture = textura
                    self.list_blocks.append(sprite)


class WallManager():
    def __init__(self, pos, quantity=1):
        self.wall = Wall(quantity)
        self.calcular_distribucion()
        # calcular cuantos
        lista_walls = []
        for index in range(quantity)
            lista_walls.append(copy(self.wall))

        self.block_list = arcade.SpriteList()


    def calcular_distribucion(self):
        """
        En base a valor de atributo quantity y el tamaño de la pantalla calculamos la posicion de cada elemento
        :return: Nada
        """
        ancho_rectangulo = (SCREEN_WIDTH - SCREEN_MARGIN) / self.quantity




