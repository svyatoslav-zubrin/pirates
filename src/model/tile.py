import pygame
from enum import Enum

class Tile:
    def __init__(self, size, position):
        """ Creates new Tile object

        Parameters:
            size (int, int): size of the tile (width, height), px
            position (int, int): position of the tile on the map (x, y)

        Returns:
            New Tile object.
        """
        self.size = size
        self.position = position
        self.inactive_border_color = (0, 0, 0)
        self.active_border_color = (255, 0, 0)
        self.isActive = False

    def configure(self, tile_cfg):
        self.bg_color = tile_cfg.color()

    def render(self, screen):
        bg_rect = (self.position[0] * self.size[0],
                   self.position[1] * self.size[1],
                   self.size[0],
                   self.size[1])
        pygame.draw.rect(screen,
                         self.bg_color,
                         bg_rect)

        br_rect = (self.position[0] * self.size[0],
                   self.position[1] * self.size[1],
                   self.size[0] - 1,
                   self.size[1] - 1)
        pygame.draw.rect(screen,
                         self.__border_color(),
                         br_rect,
                         self.__border_width())

    def __border_color(self):
        if self.isActive:
            return self.active_border_color
        else:
            return self.inactive_border_color

    def __border_width(self):
        if self.isActive:
            return 3
        else:
            return 1


class TileType(Enum):
    WATER = '.'
    GRASS = 'g'
    WHARF = 'w'
    NEUTRAL_TRADE = 't'
    NEUTRAL_MILITARY = 'm'


class TileCfg:
    def __init__(self, tile_id):
        self.type = TileType(tile_id)

    def color(self):
        if self.type == TileType.WATER:
            return (173, 216, 230)  # blue
        if self.type == TileType.WHARF:
            return (139, 69, 19)  # brown
        if self.type == TileType.NEUTRAL_TRADE:
            return (70, 130, 180)  # brown
        if self.type == TileType.NEUTRAL_MILITARY:
            return (70, 130, 180)  # brown
        else:
            return (34, 139, 34)  # green
