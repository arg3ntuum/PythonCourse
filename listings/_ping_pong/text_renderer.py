import pygame


class TextRenderer:
    def __init__(self, font, color):
        self._font = font
        self._color = color

    def render(self, text, screen, position):
        rendered_text = self.font.render(text, True, self.color)
        screen.blit(rendered_text, position)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        self._font = font

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color