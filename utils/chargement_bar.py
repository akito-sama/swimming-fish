import pygame
from pygame.locals import *


class LoadingBar:

    def __init__(self, fish):
        self.fish = fish
        self.value = 0

    def draw(self):
        pygame.draw.rect(
            self.fish.game.screen,
            "#9c27e6",
            (self.fish.x + 5, self.fish.y - 10, self.fish.height, self.fish.width - 10))

        pygame.draw.rect(
            self.fish.game.screen,
            "#595959",
            (self.fish.x + 5, self.fish.y - 10, self.fish.height, self.fish.width - 10))

    def charge(self, amount):
        self.value = amount
