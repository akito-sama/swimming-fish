import pygame
from utils.chargement_bar import LoadingBar


class Fish:

    def __init__(self, game):
        self.game = game
        self.x = 200
        self.y = 200
        self.width, self.height = 20, 20
        self.charge_bar = LoadingBar(self)

    def draw(self):
        self.charge_bar.draw()
        pygame.draw.rect(self.game.screen, "#52a2da", (self.x, self.y, 20, 20), border_radius=5)

    def event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass

    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.charge_bar.charge(5)
