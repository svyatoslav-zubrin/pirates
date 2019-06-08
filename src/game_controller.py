import pygame
from pygame import Rect
from model.map import Map


class GameController:
    def __init__(self, size, title):
        self.size = size
        self.title = title
        self.map_grid_size = 22
        self.map_rect = Rect((0, 0), (self.size[1], self.size[1]))

    def start(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        map = Map(self.map_rect, self.map_grid_size)

        running = True
        while running:
            map.render(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if self.map_rect.collidepoint(position):
                        map.handle_click(position)
            pygame.display.flip()


windowSize = (1000, 800)

game_controller = GameController(windowSize, 'Пiрати')
game_controller.start()
