import pygame


class Tile:
    def __init__(self, bg_color, size, position):
        """ Creates new Tile object

        Parameters:
            bg_color (color): tile's background color
            size (int, int): size of the tile (width, height), px
            position (int, int): position of the tile on the map (x, y)

        Returns:
            New Tile object.
        """
        self.bg_color = bg_color
        self.size = size
        self.position = position
        self.inactive_border_color = (0, 0, 0)
        self.active_border_color = (255, 0, 0)
        self.isActive = False

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
