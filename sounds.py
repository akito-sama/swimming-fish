import pygame
pygame.mixer.init()

into_water = pygame.mixer.Sound("sounds/into water.wav")
out_of_water = pygame.mixer.Sound("sounds/jumping.wav")
coin_sound = pygame.mixer.Sound("sounds/sound coins.wav")
coin_sound.set_volume(0.2)
