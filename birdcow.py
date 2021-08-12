import pygame
import customevents


class BirdCow:

    def __init__(self, game, coordinate, velocity: int):
        x, y = coordinate
        self.game = game
        self.image = self.game.mono_surfaces.bird_surface
        self.rect: pygame.Rect = self.image.get_rect(x=x, y=y)
        self.velocity = velocity

    def move(self):
        self.rect.x -= self.velocity
        if self.rect.colliderect(self.game.fish.rect):
            pygame.event.post(pygame.event.Event(customevents.END_EVENT))
        if self.rect.x <= 0:
            self.game.all_birds.remove(self)
            pygame.event.post(pygame.event.Event(customevents.SPAWN_BIRD_EVENT))

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

