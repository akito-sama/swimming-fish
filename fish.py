import pygame
from utils.chargement_bar import LoadingBar
from utils.rotator import Rotator
from utils.gravity import Gravity
import sounds


class Fish:

    def __init__(self, game):
        self.x_velocity = 5
        self.game = game
        self.x = 200
        self.initial_y = self.game.screen.get_height() - self.game.mono_surfaces.water.get_height() / 2
        self.rotator = Rotator(self, "images/doripi.png", 2)
        self.width, self.height = self.rotator.image.get_size()
        self.rect = self.rotator.image.get_rect(x=self.x, y=self.initial_y)
        self.charge_bar = LoadingBar(self)
        self.gravity = Gravity(self)
        self.state = "swimming"
        self.list_verified = []

    def draw(self):
        self.charge_bar.draw()
        self.game.screen.blit(self.rotator.image, self.rect)
        pygame.draw.rect(self.game.screen, (0, 255, 0), self.rect, 3)

    def update(self, tick):
        pressed = pygame.key.get_pressed()
        # loading bar management
        if pressed[pygame.K_SPACE] and self.state == "swimming":
            self.charge_bar.charge(5)
            if self.charge_bar.value != self.charge_bar.limit:
                self.rect.y += 1
                if self.rotator.angle > -90:
                    self.rotator.angle -= self.rect.y / (self.game.mono_surfaces.water.get_width() / 2)
            self.rotator.rotate()
        elif self.charge_bar.value > 0:
            if self.state == "swimming":
                self.gravity.reset(y=self.charge_bar.value * 1.4)
                self.state = "jumping"
            self.charge_bar.charge(-5)
            if self.charge_bar.value <= 0:
                self.charge_bar.value = 0
            self.rotator.angle += 0.9
            self.rotator.rotate()
            self.gravity.applicate(tick)
        elif self.state == "jumping":
            self.gravity.applicate(tick)
            if self.rotator.angle < 0:
                self.rotator.angle += 2
            self.rotator.rotate()

        elif self.state == "falling":
            self.gravity.applicate(tick)
            if self.initial_y <= self.rect.y:
                self.rect.y = self.game.screen.get_height() - self.game.mono_surfaces.water.get_height() / 2
                self.gravity.reset(y=self.charge_bar.value * 1.3)
                self.state = "swimming"
            elif self.game.screen.get_height() - self.game.mono_surfaces.water.get_height() <= self.rect.y:
                if self.rotator.angle <= 0:
                    self.rotator.angle += 4.5
                # sounds.into_water.play()
                pygame.mixer.music.unpause()
            else:
                self.rotator.angle -= 0.6
            self.rotator.rotate()

        # movements
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

        self.points()

    def reset(self):
        self.x = 200
        self.rect = self.rotator.image.get_rect(x=self.x, y=self.initial_y)
        self.charge_bar.reset()
        self.gravity.reset()
        self.state = "swimming"
        self.list_verified = []

    def points(self):
        for obstacle in self.game.obstacles:
            if obstacle not in self.list_verified:
                if obstacle.down_rectangle.x < self.rect.x + self.rotator.image.get_width() // 2 and obstacle.up_rectangle.y + obstacle.up_rectangle.width < self.rect.y < obstacle.down_rectangle.y:
                    self.game.score.add_score(10)
                    sounds.coin_sound.play()
                    self.list_verified.append(obstacle)
