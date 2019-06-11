import os
import random
import pygame


class Dice(pygame.sprite.DirtySprite):
    def __init__(self, rect):
        super(Dice, self).__init__()

        self.rect = rect
        self.value = 0
        self.image = self.__image(rect.size)

    def roll(self):
        self.value = random.randint(1, 6)
        self.image = self.__image(self.rect.size)
        self.dirty = 1
        return self.value

    def reset(self):
        self.value = 0
        self.dirty = 1

    def __image(self, size):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        image_name = ["../../assets/dice/dice_0.png",
                      "../../assets/dice/dice_1.png",
                      "../../assets/dice/dice_2.png",
                      "../../assets/dice/dice_3.png",
                      "../../assets/dice/dice_4.png",
                      "../../assets/dice/dice_5.png",
                      "../../assets/dice/dice_6.png"]
        path = os.path.join(main_dir, image_name[self.value])
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
