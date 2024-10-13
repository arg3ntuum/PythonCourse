import random
import pygame

from _tetris.config import Config


class Shape:
    """Представляє фігуру та її положення."""

    def __init__(self):
        self.shape = random.choice(Config.get_list_shapes())
        self.position = [Config.GRID_WIDTH // 2 - len(self.shape[0]) // 2, 0]

    def rotate(self):
        """Поворот фігури на 90 градусів за годинниковою стрілкою."""

        # Крок 1: Реверс рядків фігури, змінюємо їхній порядок на протилежний.
        reversed_shape = self.shape[::-1]

        # Крок 2: Створюємо нову форму, використовуючи zip, щоб об'єднати елементи
        # з кожного рядка і перетворюємо отримані кортежі в списки.
        rotated_shape = []
        for row in zip(*reversed_shape):# Звездочка распаковывает нам елементы, типа поелементно
            rotated_shape.append(list(row))

        # Крок 3: Зберігаємо повернуту фігуру.
        self.shape = rotated_shape

    def draw(self, screen):
        """Малює фігуру на екрані."""
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x]:
                    pygame.draw.rect(
                        screen,
                        Config.get_colors()[self.shape[y][x]],
                        ((x + self.position[0]) * Config.TILE_SIZE_X,
                         (y + self.position[1]) * Config.TILE_SIZE_Y,
                         Config.TILE_SIZE_X, Config.TILE_SIZE_Y)
                    )

    def check_collision(self, grid):
        """Перевіряє наявність колізій між фігурою та сіткою."""
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x]:
                    if (x + self.position[0] < 0 or
                            x + self.position[0] >= Config.GRID_WIDTH or
                            y + self.position[1] >= Config.GRID_HEIGHT or
                            (y + self.position[1] >= 0 and grid.grid[y + self.position[1]][x + self.position[0]] != 0)):
                        return True
        return False
