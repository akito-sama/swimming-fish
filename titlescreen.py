import pygame

pygame.font.init()

title_font = pygame.font.Font("fonts/Mighty Kingdom.ttf", 50)


class TitleScreen:

    def __init__(self, game):
        self.game = game
        self.surface_title = title_font.render("Dori From Wish !!", True, (255, 255, 255))
        self.white_surface_title = self.surface_title.copy()
        self.yellow_surface_title = title_font.render("Dori From Wish !!", True, "#fdd835")
        x = game.screen_width//2 - self.surface_title.get_width()//2
        y = game.screen_height//2 - self.surface_title.get_height()//2 + 30
        self.surface_title_rect = self.surface_title.get_rect(x=x, y=y)

        button_surface = pygame.image.load("images/playbutton.png").convert_alpha()
        self.button_surface = pygame.transform.scale(button_surface, (button_surface.get_width() * 3, button_surface.get_height() * 3))
        self.button_rect = self.button_surface.get_rect(x=x + 100, y=y + 100)

    def event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.game.reset()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.surface_title_rect.collidepoint(mouse_pos):
            self.surface_title = self.yellow_surface_title
        else:
            self.surface_title = self.white_surface_title

    def draw(self):
        self.game.screen.blit(self.game.mono_surfaces.background, (0, 0))
        self.game.screen.blit(self.surface_title, self.surface_title_rect)
        self.game.screen.blit(self.button_surface, self.button_rect)
