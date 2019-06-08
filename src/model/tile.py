import pygame
from enum import Enum


class Tile(pygame.sprite.DirtySprite):
    def __init__(self, size, position, cfg):
        """ Creates new Tile object

        Parameters:
            size (int, int): size of the tile (width, height), px
            position (int, int): position of the tile on the map (x, y)
            cfg (TileCfg): config for the tile
        Returns:
            New Tile object.
        """
        super(Tile, self).__init__()

        # model
        self.size = size
        self.position = position

        self.isSailable = cfg.isSailable()

        self.inactive_border_color = (0, 0, 0)
        self.active_border_color = (255, 0, 0)

        # UI
        self.rect = pygame.Rect(self.position[0] * self.size[0],
                                self.position[1] * self.size[1],
                                self.size[0],
                                self.size[1])
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(cfg.color())

    def update(self):
        self.__draw()

    def __draw(self):
        br_rect = (0, 0, self.size[0] - 1, self.size[1] - 1)
        pygame.draw.rect(self.image,
                         self.inactive_border_color,
                         br_rect,
                         1)


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
        elif self.type == TileType.WHARF:
            return (139, 69, 19)  # brown
        elif self.type == TileType.NEUTRAL_TRADE:
            return (70, 130, 180)  # brown
        elif self.type == TileType.NEUTRAL_MILITARY:
            return (70, 130, 180)  # brown
        else:  # grass
            return (34, 139, 34)  # green

    def isSailable(self):
        if self.type == TileType.GRASS:
            return False
        else:
            return True
