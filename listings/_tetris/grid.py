import pygame

from _tetris.config import Config


class Grid:
    """Представляє сітку, в якій розміщуються фігури."""

    def __init__(self, width, height):
        self.grid = [[0] * width for _ in range(height)]

    def draw(self, screen):
        """Малює сітку на екрані."""
        for y in range(Config.GRID_HEIGHT):
            for x in range(Config.GRID_WIDTH):
                if self.grid[y][x] != 0:
                    pygame.draw.rect(
                        screen,
                        Config.get_colors()[self.grid[y][x]],
                        (x * Config.TILE_SIZE_X, y * Config.TILE_SIZE_Y, Config.TILE_SIZE_X, Config.TILE_SIZE_Y)
                    )

    def merge_shape(self, shape, offset):
        """Додає фігуру до сітки."""
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[y][x]:
                    self.grid[y + offset[1]][x + offset[0]] = shape[y][x]

    def clear_lines(self):
        """Очищення заповнених ліній."""
        # Створюємо нову сітку з рядків, у яких є хоча б одне порожнє місце (0)
        new_grid = [row for row in self.grid if 0 in row]

        # Підраховуємо кількість очищених ліній
        lines_cleared = Config.GRID_HEIGHT - len(new_grid)

        # Додаємо зверху порожні рядки (тільки з нулями) для очищених ліній
        empty_rows = [[0] * Config.GRID_WIDTH for _ in range(lines_cleared)]

        # Оновлюємо сітку, додавши порожні рядки зверху
        self.grid = empty_rows + new_grid


