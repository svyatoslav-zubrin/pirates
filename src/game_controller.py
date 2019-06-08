import pygame
from model.ship import Ship, ShipType
from model.map import Map

class GameController:
    def __init__(self, size, title):
        self.size = size
        self.title = title
        self.map_size = 20

    def start(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        map = Map(self.size, self.map_size)

        running = True
        while running:
            map.render(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


windowSize = (800, 800)

game_controller = GameController(windowSize, 'Pirates')
game_controller.start()

