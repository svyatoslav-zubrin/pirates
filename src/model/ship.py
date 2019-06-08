import pygame
from enum import Enum

class Ship:
    def __init__(self, type):
        self.type = type
        self.x = 0
        self.y = 0
        self.size = 10

    def move(self, screen, cell_size, position):
        self.x = position[0]
        self.y = position[1]
        self.render(screen, cell_size)

    def render(self, screen, cell_size):
        pygame.draw.circle(screen,
                           self._color(),
                           (self.x * cell_size + cell_size // 2,
                            self.y * cell_size + cell_size // 2),
                           self.size, 1)

    def _color(self):
        if self.type is ShipType.PIRATE:
            return (0, 255, 0)
        elif self.type is ShipType.MILITARY:
            return (255, 0, 0)
        else:
            return (0, 0, 255)

class ShipType(Enum):
    PIRATE = 1
    MILITARY = 2
    MERCHANT = 3

