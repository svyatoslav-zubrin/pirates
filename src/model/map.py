import pygame
from .tile import Tile, TileCfg
from .ship import Ship
from .player import Player

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

        self.tiles_group = pygame.sprite.LayeredDirty()

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
                self.tiles_group.add(tile)

        # ships
        self.ships = {}

    def constructShips(self, players):
        total = len(self.ships) + len(players)
        if total >= len(Map.initial_ship_positions):
            return False

        for player in players:
            ship = self.__constructShip(player, len(self.ships))
            self.ships[player.name] = ship
            self.tiles_group.add(ship)

    def handle_click(self, position, player):
        y = position[1] // (self.size[1] // self.grid_size)
        x = position[0] // (self.size[0] // self.grid_size)
        tile = self.tiles[x][y]

        if tile.isSailable:
            ship = self.ships[player.name]
            ship.move(tile.position)

    def __tile_size(self):
        return (self.size[0] // self.grid_size,
                self.size[1] // self.grid_size)

    def __constructShip(self, player, index):
        index = len(self.ships)
        pos = Map.initial_ship_positions[index]
        return Ship(self.__tile_size(), pos, index)
