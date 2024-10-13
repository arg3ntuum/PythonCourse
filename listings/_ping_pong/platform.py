import pygame

class Platform:
    def __init__(self, x, y, width, height, speed):
        self._rect = pygame.Rect(x, y, width, height)
        self._speed = speed

    def move_up(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed

    def move_down(self, screen_height):
        if self.rect.bottom < screen_height:
            self.rect.bottom += self.speed

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed