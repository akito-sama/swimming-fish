import pygame


class MonoSurfaces:
    """this class contains the surface of the gameplay based on the screen
    of the game and also don't needed surfaces that is there for the
    decoration"""

    def __init__(self, screen_width, screen_height):
        self.screen_height = screen_height
        self.screen_width = screen_width

        # --------------- water ---------------
        self.water = pygame.Surface((self.screen_width, (screen_height / 2.3)))
        self.water.fill((91, 162, 200))
        # self.water.set_colorkey((0, 0, 0))
        pygame.draw.line(self.water, (255, 255, 255), (0, 0), (screen_width, 0), 5)
        # self.water.set_alpha(80)

        # --------------- pic ------------------
        self.pic = pygame.transform.scale2x(pygame.image.load(
            "images/Mountain.png" if not __name__ == "__main__" else "../images/Mountain.png"
            )).convert_alpha()
        self.up_pic = pygame.transform.rotate(self.pic, 180)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    running = True
    mono_surfaces = MonoSurfaces(300, 300)

    while running:
        screen.fill((0, 0, 0))
        screen.blit(mono_surfaces.water, (0, 200))
        screen.blit(mono_surfaces.up_pic, (200, 0))
        screen.blit(mono_surfaces.pic, (200, 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
