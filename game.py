import pygame
from pygame.locals import *
from fish import Fish
from utils.surfaces import MonoSurfaces


class Game:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.mono_surfaces = MonoSurfaces(*screen.get_size())
        self.screen_width, self.screen_height = screen.get_size()
        self.running = True
        self.fish = Fish(self)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.mono_surfaces.water,
                         (0, self.screen_height - self.mono_surfaces.water.get_height()))
        self.fish.draw()
        pygame.display.update()
    
    def update(self, tick):
        self.fish.update(tick)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            
