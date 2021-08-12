import pygame


class MonoSurfaces:
    """this class contains the surface of the gameplay based on the screen
    of the game and also don't needed surfaces that is there for the
    decoration"""

    def __init__(self, game, screen_width, screen_height):
        self.screen_height = screen_height
        self.screen_width = screen_width

        # --------------- water ---------------
        self.water = pygame.Surface((self.screen_width, (screen_height / 2.3)))
        self.water.fill((91, 162, 200))
        self.water_rect = self.water.get_rect(x=0, y=game.screen_height - self.water.get_height())
        pygame.draw.line(self.water, (255, 255, 255), (0, 0), (screen_width, 0), 5)
        # self.water.set_alpha(200)

        # --------------- pic ------------------
        self.pic = pygame.transform.scale2x(pygame.image.load(
            "images/Mountain.png" if not __name__ == "__main__" else "../images/Mountain.png"
        )).convert_alpha()
        self.up_pic = pygame.transform.rotate(self.pic, 180)
        # ------------- background ---------------
        self.background = pygame.transform.scale(
            pygame.image.load("images/background.png"), (self.screen_width, self.screen_height)
        ).convert()
        # -------------- bird --------------------
        self.bird_surface = pygame.image.load("images/bird cow.png")
        self.bird_surface = pygame.transform.scale(self.bird_surface, (round(self.bird_surface.get_width() * 2.5),
                                                                       round(self.bird_surface.get_height() * 2.5))
                                                   ).convert_alpha()


"""
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
"""
