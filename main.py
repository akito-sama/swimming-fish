import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((1366, 768))
print(screen.get_size())
pygame.display.set_caption("swimming-fish")
clock = pygame.time.Clock()
game = Game(screen)

while game.running:
    clock.tick(60)
    game.draw()
    game.update(clock.get_time() / 1000)
    game.event()
