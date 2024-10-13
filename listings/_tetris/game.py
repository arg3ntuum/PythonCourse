from _tetris.game_screen import GameScreen
from _tetris.config import Config
from _tetris.grid import Grid
from _tetris.shape import Shape
import pygame

class Game:
    """Основний клас для керування грою."""

    def __init__(self):
        self.screen = GameScreen(Config.WIDTH, Config.HEIGHT)
        self.grid = Grid(Config.GRID_WIDTH, Config.GRID_HEIGHT)
        self.current_shape = Shape()
        self.game_over = False

    def handle_input(self):
        """Обробка вводу з клавіатури."""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quit_game()
                case pygame.KEYDOWN:
                    self.handle_keydown(event.key)

    def handle_keydown(self, key):
        """Обробка натискань клавіш."""
        match key:
            case pygame.K_LEFT:
                self.move_shape(-1, 0)  # Зсув вліво
            case pygame.K_RIGHT:
                self.move_shape(1, 0)  # Зсув вправо
            case pygame.K_DOWN:
                self.move_shape(0, 1)  # Зсув вниз
            case pygame.K_UP:
                self.rotate_shape()  # Поворот

    def move_shape(self, dx, dy):
        """Перемістити фігуру на dx, dy."""
        self.current_shape.position[0] += dx
        self.current_shape.position[1] += dy
        if self.current_shape.check_collision(self.grid):
            self.current_shape.position[0] -= dx
            self.current_shape.position[1] -= dy

    def rotate_shape(self):
        """Повернути фігуру."""
        self.current_shape.rotate()
        if self.current_shape.check_collision(self.grid):
            self.current_shape.rotate()  # Повернути назад, якщо колізія

    def quit_game(self):
        """Вихід з гри."""
        pygame.quit()
        exit()

    def update(self):
        """Оновлення стану гри."""
        self.current_shape.position[1] += 1
        if self.current_shape.check_collision(self.grid):
            self.current_shape.position[1] -= 1
            self.grid.merge_shape(self.current_shape.shape, self.current_shape.position)
            self.grid.clear_lines()
            self.current_shape = Shape()
            if self.current_shape.check_collision(self.grid):
                self.game_over = True

    def draw(self):
        """Малювання гри на екрані."""
        self.screen.clear(Config.get_colors().pop(0))
        self.grid.draw(self.screen.screen)
        self.current_shape.draw(self.screen.screen)
        self.screen.update()

    def run(self):
        """Основний цикл гри."""
        while not self.game_over:
            self.handle_input()
            self.update()
            self.draw()
            self.screen.clock.tick(10)
        pygame.quit()
