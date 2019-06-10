import pygame
import os
# from enum import Enum


class Ship(pygame.sprite.DirtySprite):
    ship_icons = [
        "../../assets/icons8-historic-ship-48.png",
        "../../assets/ship_from_kids_48.png"
    ]

    def __init__(self, size, position, player_number):
        super(Ship, self).__init__()

        self.size = size
        self.image = self.__image(self.size, player_number)
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

    def __image(self, size, player_number):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        image_name = Ship.ship_icons[player_number % len(Ship.ship_icons)]
        path = os.path.join(main_dir, image_name)
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)


# class ShipType(Enum):
#     PIRATE = 1
#     MILITARY = 2
#     MERCHANT = 3
