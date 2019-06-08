from .tile import Tile, TileCfg


Initial_Board = [
    ['g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g', 'g', 'g', 'g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g'],  # nopep8
    ['g', 'w', '.', '.', '.', '.', '.', '.', '.', 'w', 'g', 'g', 'w', '.', '.', '.', '.', '.', '.', '.', 'w', 'g'],  # nopep8
    ['.', '.', 't', '.', '.', '.', '.', '.', '.', 't', 'w', 'w', 't', '.', '.', '.', '.', '.', '.', 't', '.', '.'],  # nopep8
    ['.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 't', 'w', '.', 't', '.', '.', '.', '.', '.', '.', 't', '.', 'w', 't', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 'w', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', 'w', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 't', '.', '.', 'm', '.', '.', '.', '.', '.', '.', 'm', '.', '.', 't', '.', '.', '.', '.'],  # nopep8
    ['g', '.', '.', 't', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 't', '.', '.', 'g'],  # nopep8
    ['g', 'w', 't', '.', '.', '.', '.', '.', '.', 'm', 'w', 'w', 'm', '.', '.', '.', '.', '.', '.', 't', 'w', 'g'],  # nopep8
    ['g', 'g', 'w', '.', '.', '.', '.', '.', '.', 'w', 'g', 'g', 'w', '.', '.', '.', '.', '.', '.', 'w', 'g', 'g'],  # nopep8
    ['g', 'g', 'w', '.', '.', '.', '.', '.', '.', 'w', 'g', 'g', 'w', '.', '.', '.', '.', '.', '.', 'w', 'g', 'g'],  # nopep8
    ['g', 'w', 't', '.', '.', '.', '.', '.', '.', 'm', 'w', 'w', 'm', '.', '.', '.', '.', '.', '.', 't', 'w', 'g'],  # nopep8
    ['g', '.', '.', 't', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 't', '.', '.', 'g'],  # nopep8
    ['.', '.', '.', '.', 't', '.', '.', 'm', '.', '.', '.', '.', '.', '.', 'm', '.', '.', 't', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 'w', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', 'w', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 't', 'w', '.', 't', '.', '.', '.', '.', '.', '.', 't', '.', 'w', 't', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.'],  # nopep8
    ['.', '.', 't', '.', '.', '.', '.', '.', '.', 't', 'w', 'w', 't', '.', '.', '.', '.', '.', '.', 't', '.', '.'],  # nopep8
    ['g', 'w', '.', '.', '.', '.', '.', '.', '.', 'w', 'g', 'g', 'w', '.', '.', '.', '.', '.', '.', '.', 'w', 'g'],  # nopep8
    ['g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g', 'g', 'g', 'g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g']   # nopep8
]


class Map:
    def __init__(self, rect):
        """ Constructs new Map object.

        Parameters:
            rect (Rect): rect of the map ((x, y), (width, height)), px

        Returns:
            New map object
        """
        self.size = rect.size
        self.grid_size = 22

        self.tiles = [[] for _ in range(self.grid_size)]
        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                tile_size = (self.size[0] // self.grid_size,
                             self.size[1] // self.grid_size)
                position = (i, j)
                tile = Tile(tile_size, position)
                self.__configureTile(tile)
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

    def __configureTile(self, tile):
        tile_id = Initial_Board[tile.position[0]][tile.position[1]]
        tile_cfg = TileCfg(tile_id)
        tile.configure(tile_cfg)
