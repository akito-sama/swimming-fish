import pygame
from fish import Fish
from utils.surfaces import MonoSurfaces
from obstacle import Obstacle
import customevents
import random
from titlescreen import TitleScreen
from scorelabel import Score


class Game:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.mono_surfaces = MonoSurfaces(self, *screen.get_size())
        self.running = True
        self.score = Score(self)
        self.fish = Fish(self)
        self.obstacles = []
        self.spawn_obstacle()
        self.title_screen = TitleScreen(self)
        self.state = "title screen"
        pygame.mixer.music.load("sounds/background.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw(self):
        if self.state == "in game":
            self.screen.fill((0, 0, 0))
            for obstacle in self.obstacles:
                obstacle.draw()
            self.screen.blit(self.mono_surfaces.water, self.mono_surfaces.water_rect)
            self.fish.draw()
            if self.obstacles:
                pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles[0].up_rectangle, 1)
                pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles[0].down_rectangle, 1)
            self.score.draw()

        elif self.state == "title screen":
            self.title_screen.draw()

        pygame.display.update()
    
    def update(self, tick):
        if self.state == "in game":
            self.fish.update(tick)
            for obstacle in self.obstacles:
                obstacle.move()

        elif self.state == "title screen":
            self.title_screen.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            if self.state == "in game":
                if event.type == customevents.SPAWN_OBSTACLE_EVENT:
                    self.spawn_obstacle()
                if event.type == customevents.END_EVENT:
                    self.state = "title screen"
            elif self.state == "title screen":
                self.title_screen.event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

    def spawn_obstacle(self):
        self.obstacles.append(Obstacle(self, random.randint(-100, 0), random.randint(350, 400)))

    def reset(self):
        self.obstacles = []
        self.spawn_obstacle()
        self.score.reset()
        self.fish.reset()
        self.state = "in game"
