import os
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
        bg_image = cfg.image(size)
        if bg_image is None:
            self.image = pygame.Surface(self.rect.size)
            self.image.fill(cfg.color())
        else:
            self.image = bg_image

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
    NEUTRAL_TRADE = 't'
    NEUTRAL_MILITARY = 'm'
    # wharfs
    WHARF_LEFT = '←'
    WHARF_RIGHT = '→'
    WHARF_UP = '↑'
    WHARF_DOWN = '↓'
    WHARF_TOP_LEFT = '↖︎'
    WHARF_TOP_RIGHT = '↗︎'
    WHARF_BOTTOM_LEFT = '↙︎'
    WHARF_BOTTOM_RIGHT = '↘︎'


class TileCfg:
    def __init__(self, tile_id):
        self.type = TileType(tile_id)

    def color(self):
        if self.type == TileType.WATER:
            return (173, 216, 230)  # blue
        elif self.type == TileType.GRASS:
            return (34, 139, 34)  # green
        elif self.type == TileType.NEUTRAL_TRADE:
            return (70, 130, 180)  # dark blue
        elif self.type == TileType.NEUTRAL_MILITARY:
            return (70, 130, 180)  # dark blue
        else:  # wharfs
            return (139, 69, 19)  # brown

    def image(self, size):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        if self.type == TileType.GRASS:
            path = os.path.join(main_dir, '../../assets/grass1.png')
            image = pygame.image.load(path)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WATER:
            path = os.path.join(main_dir, '../../assets/water_light.png')
            image = pygame.image.load(path)
            return pygame.transform.scale(image, size)
        elif (self.type == TileType.NEUTRAL_TRADE or
                self.type == TileType.NEUTRAL_MILITARY):
            path = os.path.join(main_dir, '../../assets/water_dark.png')
            image = pygame.image.load(path)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_DOWN:
            path = os.path.join(main_dir, '../../assets/pier_s.png')
            image = pygame.image.load(path)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_UP:
            path = os.path.join(main_dir, '../../assets/pier_s.png')
            image = pygame.image.load(path)
            image = pygame.transform.flip(image, False, True)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_LEFT:
            path = os.path.join(main_dir, '../../assets/pier_s.png')
            image = pygame.image.load(path)
            image = pygame.transform.rotate(image, -90)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_RIGHT:
            path = os.path.join(main_dir, '../../assets/pier_s.png')
            image = pygame.image.load(path)
            image = pygame.transform.rotate(image, 90)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_BOTTOM_RIGHT:
            path = os.path.join(main_dir, '../../assets/pier_d.png')
            image = pygame.image.load(path)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_BOTTOM_LEFT:
            path = os.path.join(main_dir, '../../assets/pier_d.png')
            image = pygame.image.load(path)
            image = pygame.transform.rotate(image, -90)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_TOP_LEFT:
            path = os.path.join(main_dir, '../../assets/pier_d.png')
            image = pygame.image.load(path)
            image = pygame.transform.flip(image, True, True)
            return pygame.transform.scale(image, size)
        elif self.type == TileType.WHARF_TOP_RIGHT:
            path = os.path.join(main_dir, '../../assets/pier_d.png')
            image = pygame.image.load(path)
            image = pygame.transform.rotate(image, 90)
            return pygame.transform.scale(image, size)
        else:
            return None

    def isSailable(self):
        if self.type == TileType.GRASS:
            return False
        else:
            return True
