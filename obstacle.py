import pygame
import customevents


class Obstacle:

    def __init__(self, game, y):
        self.y = y
        self.game = game
        self.velocity = 5
        self.x = self.game.screen.get_width() + 50

    def move(self):
        if self.x > -self.game.screen_width / 10:
            self.x -= self.velocity
        else:
            self.game.obstacles.remove(self)
            pygame.event.post(pygame.event.Event(customevents.SPAWN_OBSTACLE_EVENT))

    def draw(self):
        self.game.screen.blit(self.game.mono_surfaces.up_pic, (self.x, self.y))
        self.game.screen.blit(self.game.mono_surfaces.pic, (self.x, self.y + 350))

    def check_collision(self):
        pass
