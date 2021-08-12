import pygame
from fish import Fish
from utils.surfaces import MonoSurfaces
from obstacle import Obstacle
import customevents
import random
from titlescreen import TitleScreen
from scorelabel import Score
from birdcow import BirdCow


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
        self.all_birds = []
        self.spawn_bird()
        pygame.mixer.music.load("sounds/background.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw(self):
        if self.state == "in game":
            self.screen.blit(self.mono_surfaces.background, (0, 0))
            for obstacle in self.obstacles:
                obstacle.draw()
            self.screen.blit(self.mono_surfaces.water, self.mono_surfaces.water_rect)
            for bird in self.all_birds:
                bird.draw()
            self.fish.draw()
            self.score.draw()

        elif self.state == "title screen":
            self.title_screen.draw()
            if self.score.score != 0:
                self.score.draw()

        pygame.display.update()
    
    def update(self, tick):
        if self.state == "in game":
            self.fish.update(tick)
            for obstacle in self.obstacles:
                obstacle.move()
            for bird in self.all_birds:
                bird.move()

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
                    self.score.update_surface(True)
                if event.type == customevents.SPAWN_BIRD_EVENT:
                    self.spawn_bird()
            elif self.state == "title screen":
                self.title_screen.event(event)

    def spawn_obstacle(self):
        self.obstacles.append(Obstacle(self, random.randint(-100, 0), random.randint(350, 400)))

    def reset(self):
        self.obstacles = []
        self.all_birds = []
        self.spawn_obstacle()
        self.spawn_bird()
        self.score.reset()
        self.fish.reset()
        self.state = "in game"

    def spawn_bird(self):
        self.all_birds.append(BirdCow(self, (
            random.randint(self.screen_width, self.screen_width + random.randint(0, 300)),
            random.randint(self.mono_surfaces.water_rect.y, self.screen_height - self.mono_surfaces.bird_surface.get_height())
        ), random.randint(4, 8)))
