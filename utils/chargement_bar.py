import pygame
from pygame.locals import *


class LoadingBar:

    def __init__(self, fish):
        self.fish = fish
        self.value = 0
        self.limit = self.fish.game.screen.get_height() / 2.5

    def draw(self):
        pygame.draw.rect(
            self.fish.game.screen,
            "#595959",
            (0, 0, 15, round(self.limit)))

        pygame.draw.rect(
            self.fish.game.screen,
            "#ffcc00",
            (0, 0, 15, round(self.value)))

    def charge(self, amount):
        if 0 <= self.value <= self.limit:
            self.value += amount
            if not 0 <= self.value <= self.limit:
                if 0 < self.value:
                    self.value = self.limit
                elif self.limit < self.value:
                    self.value = 0

    def reset(self):
        self.value = 0
