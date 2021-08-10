import pygame
from pygame.locals import *
from fish import Fish


class Game:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.running = True
        self.fish = Fish(self)
        self.current_tick = 0

    def draw(self):
        self.fish.draw()
        pygame.display.update()
    
    def update(self, tick):
        self.fish.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            
