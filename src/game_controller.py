import pygame
from model.ship import Ship, ShipType

class GameController:
    def __init__(self, size, bg_color, title):
        self.size = size
        self.bg_color = bg_color
        self.title = title
        self.grid = 20 # cells number (grid x grid)
        self.ship = Ship(ShipType.PIRATE, )

    def start(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        screen.fill(self.bg_color)

        ship = Ship(ShipType.PIRATE)
        # ship.move(screen, self.size[0] / self.grid, (0, 0))

        self._draw_grid(screen)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._handleMouseClick(screen, pygame.mouse.get_pos())

    def _draw_grid(self, screen):
        width = self.size[0]
        height = self.size[1]

        for i in range(0, self.grid + 1): # horizontal
            y = height * i / self.grid
            pygame.draw.line(screen, (0, 0, 0), [0, y], [width, y], 1)

        for i in range(0, self.grid + 1): # horizontal
            x = width * i / self.grid
            pygame.draw.line(screen, (0, 0, 0), [x, 0], [x, height], 1)

    def _handleMouseClick(self, screen, position):
        cell_size = self.size[0] // self.grid
        x_index = position[0] // cell_size
        y_index = position[1] // cell_size
        self.ship.move(screen, cell_size, (x_index, y_index))
        pygame.display.flip()


bg_color = (130, 130, 130)
(width, height) = (800, 800)

game_controller = GameController((width, height), bg_color, 'Pirates')
game_controller.start()

