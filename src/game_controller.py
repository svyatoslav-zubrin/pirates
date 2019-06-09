import pygame
from pygame import Rect
from model.map import Map
from model.dice import Dice


class GameController:
    def __init__(self, size, title):
        self.size = size
        self.title = title
        self.map_rect = Rect((0, 0), (self.size[1], self.size[1]))
        self.dice_rect = Rect((self.size[1] + 50, 50), (200, 200))

        self.all_sprites_group = pygame.sprite.LayeredDirty()

    def start(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        map = Map(self.map_rect)
        dice = Dice(self.dice_rect)

        self.all_sprites_group.add(map.tiles_group.sprites())
        self.all_sprites_group.add(dice)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if self.map_rect.collidepoint(position):
                        map.handle_click(position)
                    elif self.dice_rect.collidepoint(position):
                        dice.roll()
            # Draw everything
            self.all_sprites_group.update()
            rects = self.all_sprites_group.draw(screen)
            pygame.display.update(rects)


windowSize = (1202, 902)

game_controller = GameController(windowSize, 'Пiрати')
game_controller.start()
