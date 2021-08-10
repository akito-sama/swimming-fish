import pygame
import pygame.display
import pygame.event

class Game:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.running = True
    
    def draw(self):
        self.screen.fill((0, 0 ,0))
        pygame.display.update()
    
    def update(self):
        pass

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            
