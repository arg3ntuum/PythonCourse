import pygame
class Controller:
    def __init__(self, game):
        self._game = game

    def do(self, keys):
        if keys[pygame.K_UP]:
            self.game.platform_right.move_up()
        if keys[pygame.K_DOWN]:
            self.game.platform_right.move_down(self.game.config.SCREEN_HEIGHT)
        if keys[pygame.K_w]:
            self.game.platform_left.move_up()
        if keys[pygame.K_s]:
            self.game.platform_left.move_down(self.game.config.SCREEN_HEIGHT)

    @property
    def game(self):
        return self._game;

    @game.setter
    def game(self, game):
        self._game = game