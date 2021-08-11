import pygame
from utils.chargement_bar import LoadingBar
from utils.rotator import Rotator


class Fish:

    def __init__(self, game):
        self.x_velocity = 2
        self.game = game
        self.x = 200
        self.y = self.game.screen.get_height() / 1.5
        self.rotator = Rotator(self, "images/depy nemo.png")
        self.width, self.height = self.rotator.image.get_size()
        self.rect = self.rotator.image.get_rect(x=self.x, y=self.y)
        self.charge_bar = LoadingBar(self)

    def draw(self):
        self.charge_bar.draw()
        self.game.screen.blit(self.rotator.image, self.rect)

    def event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass

    def update(self):
        pressed = pygame.key.get_pressed()
        # loading bar management
        if pressed[pygame.K_SPACE]:
            self.charge_bar.charge(5)
            self.rotator.rotate()
        elif self.charge_bar.value > 0:
            self.charge_bar.charge(-5)
            if self.charge_bar.value <= 0:
                self.charge_bar.value = 0
            self.rotator.rotate()

        # mouvements
        if pressed[pygame.K_RIGHT]:
            self.rect.x += self.x_velocity
            limited_x = self.game.screen_width - self.game.screen_width / 6 - self.width
            if self.rect.x >= limited_x:
                self.rect.x = limited_x

        elif pressed[pygame.K_LEFT]:
            self.rect.x -= self.x_velocity
            limited_x = 0
            if self.rect.x <= limited_x:
                self.rect.x = limited_x

