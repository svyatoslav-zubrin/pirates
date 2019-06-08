from .tile import Tile


class Map:
    def __init__(self, rect, grid_size):
        """ Constructs new Map object.

        Parameters:
            size (int, int): size of the map (width, height), px
            grid_size (int): number of cells along X and Y axes
        Returns:
            New map object
        """
        self.size = rect.size
        self.grid_size = grid_size

        self.tiles = [[] for _ in range(grid_size)]
        for i in range(0, grid_size):
            for j in range(0, grid_size):
                color = (135, 206, 235)
                tile_size = (self.size[0] // grid_size,
                             self.size[1] // grid_size)
                position = (i, j)
                tile = Tile(color, tile_size, position)
                self.tiles[i].append(tile)

    def render(self, screen):
        for tiles_line in self.tiles:
            for tile in tiles_line:
                tile.render(screen)

    def handle_click(self, position):
        x = position[0] // (self.size[0] // self.grid_size)
        y = position[1] // (self.size[1] // self.grid_size)
        tile = self.tiles[x][y]
        tile.isActive = True
        # print("Will handle click at (", x, ",", y, ")")
