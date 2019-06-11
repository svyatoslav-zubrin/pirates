import pygame
from .tile import Tile, TileCfg
from .ship import Ship
from .player import Player
from .marked_tile import MarkedTile

Initial_Board = [
    ['g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g', 'g', 'g', 'g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g'],  # nopep8
    ['g', '↘︎', '.', '.', '.', '.', '.', '.', '.', '←', 'g', 'g', '→', '.', '.', '.', '.', '.', '.', '.', '↙︎', 'g'],  # nopep8
    ['.', '.', 't', '.', '.', '.', '.', '.', '.', 't', '↓', '↓', 't', '.', '.', '.', '.', '.', '.', 't', '.', '.'],  # nopep8
    ['.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 't', '↑', '.', 't', '.', '.', '.', '.', '.', '.', 't', '.', '↑', 't', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', '←', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', '→', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 't', '.', '.', 'm', '.', '.', '.', '.', '.', '.', 'm', '.', '.', 't', '.', '.', '.', '.'],  # nopep8
    ['g', '.', '.', 't', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 't', '.', '.', 'g'],  # nopep8
    ['g', '↑', 't', '.', '.', '.', '.', '.', '.', 'm', '↑', '↑', 'm', '.', '.', '.', '.', '.', '.', 't', '↑', 'g'],  # nopep8
    ['g', 'g', '→', '.', '.', '.', '.', '.', '.', '←', 'g', 'g', '→', '.', '.', '.', '.', '.', '.', '←', 'g', 'g'],  # nopep8
    ['g', 'g', '→', '.', '.', '.', '.', '.', '.', '←', 'g', 'g', '→', '.', '.', '.', '.', '.', '.', '←', 'g', 'g'],  # nopep8
    ['g', '↓', 't', '.', '.', '.', '.', '.', '.', 'm', '↓', '↓', 'm', '.', '.', '.', '.', '.', '.', 't', '↓', 'g'],  # nopep8
    ['g', '.', '.', 't', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 'm', '.', '.', '.', '.', 't', '.', '.', 'g'],  # nopep8
    ['.', '.', '.', '.', 't', '.', '.', 'm', '.', '.', '.', '.', '.', '.', 'm', '.', '.', 't', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', '.', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', '←', 'g', 'g', '.', '.', '.', '.', '.', '.', '.', '.', 'g', 'g', '→', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', '.', 't', '↓', '.', 't', '.', '.', '.', '.', '.', '.', 't', '.', '↓', 't', '.', '.', '.', '.'],  # nopep8
    ['.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.', '.', 't', '.', '.', '.'],  # nopep8
    ['.', '.', 't', '.', '.', '.', '.', '.', '.', 't', '↑', '↑', 't', '.', '.', '.', '.', '.', '.', 't', '.', '.'],  # nopep8
    ['g', '↗︎', '.', '.', '.', '.', '.', '.', '.', '←', 'g', 'g', '→', '.', '.', '.', '.', '.', '.', '.', '↖︎', 'g'],  # nopep8
    ['g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g', 'g', 'g', 'g', 'g', '.', '.', '.', '.', '.', '.', 'g', 'g']   # nopep8
]


class Map:
    initial_ship_positions = [(1, 1),
                              (20, 20),
                              (1, 20),
                              (20, 1)]

    def __init__(self, rect):
        """ Constructs new Map object.

        Parameters:
            rect (Rect): rect of the map ((x, y), (width, height)), px

        Returns:
            New map object
        """
        self.size = rect.size
        self.grid_size = 22

        self.static_tiles = pygame.sprite.LayeredDirty()

        tile_size = (self.size[0] // self.grid_size,
                     self.size[1] // self.grid_size)

        # tiles
        self.tiles = [[] for _ in range(self.grid_size)]
        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                position = (i, j)
                cfg = TileCfg(Initial_Board[j][i])
                tile = Tile(tile_size, position, cfg)

                self.tiles[i].append(tile)
                self.static_tiles.add(tile)

        # ships
        self.ships = {}

        # sailable
        self.sailable_tiles = []

    def constructShips(self, players):
        total = len(self.ships) + len(players)
        if total >= len(Map.initial_ship_positions):
            return False

        for player in players:
            ship = self.__constructShip(player, len(self.ships))
            self.ships[player.name] = ship
            self.static_tiles.add(ship)

    # Manage highlighted tiles

    def highlight(self, dice_value, position, forbidden_positions=[]):
        minx = max(0, position[0] - dice_value)
        maxx = min(self.grid_size - 1, position[0] + dice_value)
        miny = max(0, position[1] - dice_value)
        maxy = min(self.grid_size - 1, position[1] + dice_value)

        highlights = []
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                shift = abs(x - position[0]) + abs(y - position[1])
                is_sailable = self.tiles[x][y].isSailable
                if shift == dice_value and is_sailable:
                    highlights.append((x, y))

        tiles_removed = self.sailable_tiles.copy()
        self.sailable_tiles.clear()
        for highlight in highlights:
            mt = MarkedTile(self.__tile_size(), highlight)
            self.sailable_tiles.append(mt)
        return tiles_removed

    def clear_highlights(self):
        tiles_removed = self.sailable_tiles.copy()
        self.sailable_tiles.clear()
        return tiles_removed

    # User actions management

    def handle_click(self, position, player):
        x = position[0] // (self.size[0] // self.grid_size)
        y = position[1] // (self.size[1] // self.grid_size)
        for tile in self.sailable_tiles:
            if tile.position[0] == x and tile.position[1] == y:
                highlighted_tile = tile
                break
        else:
            highlighted_tile = None

        if highlighted_tile is not None:
            ship = self.ships[player.name]
            ship.move(highlighted_tile.position)
            return highlighted_tile.position
        else:
            return None

    def __tile_size(self):
        return (self.size[0] // self.grid_size,
                self.size[1] // self.grid_size)

    def __constructShip(self, player, index):
        index = len(self.ships)
        pos = Map.initial_ship_positions[index]
        return Ship(self.__tile_size(), pos, index)
