import pygame

from _tetris.config import Config
from _tetris.game import Game
from _tetris.game_screen import GameScreen
from _tetris.grid import Grid
from _tetris.shape import Shape

colors = Config.get_colors()
shapes = Config.get_list_shapes()

# Запуск гри
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
