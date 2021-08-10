import pygame
from pygame.locals import *
from game import Game

pygame.init()
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("swimming-fish")
clock = pygame.time.Clock()
game = Game(screen)

while game.running:
    clock.tick(60)
    game.draw()
    game.update(clock.get_time())
    game.event()
