import pygame
from model.ship import Ship, ShipType

class GameController:
    def __init__(self, size, title):
        self.size = size
        self.title = title

    def start(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


windowSize = (800, 800)

game_controller = GameController(windowSize, 'Pirates')
game_controller.start()

