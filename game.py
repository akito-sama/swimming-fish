import pygame
from fish import Fish
from utils.surfaces import MonoSurfaces
from obstacle import Obstacle
import customevents
import random


class Game:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.mono_surfaces = MonoSurfaces(*screen.get_size())
        self.screen_width, self.screen_height = screen.get_size()
        self.running = True
        self.fish = Fish(self)
        self.obstacles = []
        self.spawn_obstacle()
        self.state = "title screen"
        pygame.mixer.music.load("sounds/background.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for obstacle in self.obstacles:
            obstacle.draw()
        self.screen.blit(self.mono_surfaces.water,
                         (0, self.screen_height - self.mono_surfaces.water.get_height()))
        self.fish.draw()
        pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles[0].up_rectangle, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles[0].down_rectangle, 1)
        pygame.display.update()
    
    def update(self, tick):
        self.fish.update(tick)
        for obstacle in self.obstacles:
            obstacle.move()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            if event.type == customevents.SPAWN_OBSTACLE_EVENT:
                self.spawn_obstacle()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

    def spawn_obstacle(self):
        self.obstacles.append(Obstacle(self, random.randint(-100, 0), random.randint(350, 400)))

