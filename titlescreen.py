import pygame

pygame.font.init()

title_font = pygame.font.Font("fonts/Mighty Kingdom.ttf", 50)


class TitleScreen:

    def __init__(self, game):
        self.game = game
        self.surface_title = title_font.render("Dori From Wish !!", True, (200, 200, 200))
        self.white_surface_title = self.surface_title.copy()
        self.yellow_surface_title = title_font.render("Dori From Wish !!", True, "#fdd835")
        self.surface_title_rect = self.surface_title.get_rect(x=game.screen_width//2 - self.surface_title.get_width()//2,
                                                              y=game.screen_height//2 - self.surface_title.get_height()//2)

    def event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.reset()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.surface_title_rect.collidepoint(mouse_pos):
            self.surface_title = self.yellow_surface_title
        else:
            self.surface_title = self.white_surface_title

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        self.game.screen.blit(self.surface_title, self.surface_title_rect)
