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
        self.border_color = (0, 0, 0)

    def render(self, screen):
        top_left = (self.position[0] * self.size[0],
                   self.position[1] * self.size[1])
        bottom_right = ((self.position[0] + 1) * self.size[0],
                        (self.position[1] + 1) * self.size[1])
        pygame.draw.rect(screen,
                         self.bg_color,
                         (top_left[0],
                          top_left[1],
                          bottom_right[0],
                          bottom_right[1]))
        pygame.draw.rect(screen,
                         self.border_color,
                         (top_left[0],
                          top_left[1],
                          bottom_right[0],
                          bottom_right[1]),
                         1)
