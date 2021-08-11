import pygame
from pygame.locals import *


class Rotator:

    def __init__(self, fish,  path: str, coef):
        self.fish = fish
        self.original_image = pygame.image.load(path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image,
                                                     tuple(map(lambda x: x * coef, self.original_image.get_size())),
                                                     )
        self.image = self.original_image.copy()
        self.image = pygame.transform.rotate(self.original_image, -90)

    def rotate(self):
        value = round(self.fish.charge_bar.value / self.fish.charge_bar.limit * 180) - 90
        self.image = pygame.transform.rotate(self.original_image, value)
        self.fish.rect = self.image.get_rect(center=self.fish.rect.center)
