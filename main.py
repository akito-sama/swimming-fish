import pygame
from game import Game
import pygame.display

pygame.init()
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("swimming-fish")
game = Game(screen)

while game.running:
    game.draw()
    game.event()
    game.update()
