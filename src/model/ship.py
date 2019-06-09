import pygame
import os
# from enum import Enum


class Ship(pygame.sprite.DirtySprite):
    def __init__(self, size, position):
        super(Ship, self).__init__()

        self.size = size
        self.image = self.__image(self.size)
        self.rect = pygame.Rect(position[0] * self.size[0],
                                position[1] * self.size[1],
                                self.size[0],
                                self.size[1])

    def move(self, position):
        self.rect = pygame.Rect(position[0] * self.size[0],
                                position[1] * self.size[1],
                                self.size[0],
                                self.size[1])
        self.dirty = 1

    def __image(self, size):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        path = os.path.join(main_dir,
                            '../../assets/icons8-historic-ship-48.png')
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)


# class ShipType(Enum):
#     PIRATE = 1
#     MILITARY = 2
#     MERCHANT = 3
