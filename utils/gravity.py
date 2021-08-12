from pygame.math import Vector2
import pygame
import sounds


class Gravity:

    def __init__(self, fish):
        self.fish = fish
        self.gravity = Vector2(x=0, y=25)
        self.speed_velocity = Vector2(x=100, y=100)

    def applicate(self, tick):
        """calculate a jump gravity"""
        self.fish.rect.y -= Vector2(x=tick, y=tick) * self.speed_velocity
        self.speed_velocity -= tick * self.gravity * 10
        if self.speed_velocity.y < 0:
            self.fish.state = "falling"
        if self.fish.rect.y <= self.fish.game.screen.get_height() - self.fish.game.mono_surfaces.water.get_height():
            pygame.mixer.music.pause()
            # sounds.out_of_water.play()

    def reset(self, x=100, y=50):
        self.speed_velocity = Vector2(x=x, y=y)  # .normalize()

    def inverse(self):
        self.speed_velocity = -self.speed_velocity
