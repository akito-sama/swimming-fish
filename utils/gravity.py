from pygame.math import Vector2


class Gravity:

    def __init__(self, fish):
        self.fish = fish
        self.gravity = Vector2(x=0, y=10)
        self.speed_velocity = Vector2(x=1, y=1)  # .normalize()

    def applicate(self, tick):
        """calculate a jump gravity"""
        self.fish.rect.y -= Vector2(x=tick, y=tick) * self.speed_velocity
        self.speed_velocity += tick * self.gravity * 10

    def reset(self):
        self.speed_velocity = Vector2(x=1, y=1)  # .normalize()

    def inverse(self):
        self.speed_velocity = -self.speed_velocity


