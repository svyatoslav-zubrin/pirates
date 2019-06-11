import pygame


class MarkedTile(pygame.sprite.DirtySprite):
    def __init__(self, size, position):
        """ Creates new MarkedTile object

        Parameters:
            size (int, int): size of the tile (width, height), px
            position (int, int): position of the tile on the map (x, y)
        Returns:
            New Tile object.
        """
        super(MarkedTile, self).__init__()

        # model
        self.size = size
        self.position = position

        # UI
        self.rect = pygame.Rect(self.position[0] * self.size[0],
                                self.position[1] * self.size[1],
                                self.size[0],
                                self.size[1])
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((0, 255, 0))
        self.image.set_alpha(100)
