import pygame
from titlescreen import title_font
import typing


class Score:

    def __init__(self, game):
        self.game = game
        self.score = 0
        self.surface: pygame.Surface = None
        self.surface_rect: pygame.Rect = None
        self.update_surface()

    def update_surface(self):
        self.surface = title_font.render(str(self.score), True, "#f2516d")
        self.surface_rect = self.surface.get_rect(x=self.game.screen_width - self.surface.get_width(),
                                                  y=0)

    def add_score(self, amount):
        self.score += amount
        self.update_surface()

    def draw(self):
        self.game.screen.blit(self.surface, self.surface_rect)

    def reset(self):
        self.score = 0
