import pygame
import customevents


class Obstacle:

    def __init__(self, game, y, distance):
        self.game = game
        x = self.game.screen.get_width() + 50
        self.up_rectangle = self.game.mono_surfaces.up_pic.get_rect(x=x,
                                                                    y=y,
                                                                    h=self.game.mono_surfaces.up_pic.get_height())

        self.down_rectangle = self.game.mono_surfaces.pic.get_rect(x=x,
                                                                   y=y+distance,
                                                                   h=self.game.screen_height - (y+distance + self.game.mono_surfaces.water.get_height()))
        self.velocity = 5

    def move(self):
        if self.up_rectangle.x > -self.game.screen_width / 10:
            self.up_rectangle.x -= self.velocity
            self.down_rectangle.x -= self.velocity
        else:
            self.game.obstacles.remove(self)
            pygame.event.post(pygame.event.Event(customevents.SPAWN_OBSTACLE_EVENT))
        if self.check_collision():
            pygame.event.post(pygame.event.Event(customevents.END_EVENT))

    def draw(self):
        self.game.screen.blit(self.game.mono_surfaces.up_pic, self.up_rectangle)
        self.game.screen.blit(self.game.mono_surfaces.pic, self.down_rectangle)
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.up_rectangle, 1)
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.down_rectangle, 1)

    def check_collision(self):
        for rect in (self.up_rectangle, self.down_rectangle):
            if rect.colliderect(self.game.fish.rect):
                return True
        return False
