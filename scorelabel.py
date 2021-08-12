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

    def update_surface(self, add_score_label=False):
        if add_score_label:
            self.surface = title_font.render(f"your score is Score : {self.score}", True, "#f2516d")
            self.end()
        else:
            self.surface = title_font.render(str(self.score), True, "#f2516d")
            self.surface_rect = self.surface.get_rect(x=self.game.screen_width - self.surface.get_width(),
                                                        y=0)

    def add_score(self, amount):
        self.score += amount
        self.update_surface()

    def draw(self):
        self.game.screen.blit(self.surface, self.surface_rect)

    def end(self):
        self.surface_rect.x, self.surface_rect.y = (self.game.screen_width // 2 - self.surface.get_width() // 2,
                                                    self.game.screen_height // 2 - self.surface.get_height() // 2 - 200)

    def reset(self):
        self.score = 0
        self.update_surface()

