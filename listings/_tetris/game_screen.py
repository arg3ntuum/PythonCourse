import pygame


class GameScreen:
    """Відповідає за роботу з екраном."""

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()

    def clear(self, color):
        """Очищення екрану."""
        self.screen.fill(color)

    def update(self):
        """Оновлення екрану."""
        pygame.display.flip()
