import pygame
import random
class Ball:
    def __init__(self, x, y, radius, speed):
        self._rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self._radius = radius
        self._dx = random.choice([-1, 1])
        self._dy = random.choice([-1, 1])
        self._speed = speed

    def move(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

    def generate_new_direction(self):
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, value):
        self._dx = value

    @property
    def dy(self):
        return self._dy

    @dy.setter
    def dy(self, value):
        self._dy = value