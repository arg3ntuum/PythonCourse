from operator import length_hint

import pygame
import time

from _snake.UI import UI
from _snake.apples import Apple
from _snake.engine import Engine
from _snake.points import Point
from _snake.controller import Controller
from _snake.snake import Snake
from _snake.game import Game

def create_game() -> Game:
    screen_size = Point(540, 480)
    speed = 10
    game_size = 20

    game_obj = Game(screen_size=screen_size, speed=speed, game_size=game_size)
    return game_obj

def create_snake() -> Snake:
    head = [0, 0]
    default_coordinates = game.get_coordinates(cells=game.get_cells())
    length = 1
    snake_list = [[int, int]]
    directions =  Point(0, -1)

    snake_obj = Snake(head, default_coordinates, length, snake_list, directions)
    return snake_obj

def stop() -> bool:
    UI.game_over(screen, game.screen_size)
    pygame.display.flip()
    time.sleep(2)
    return False

def start_game(game, screen, controller, snake):
    game_while = True
    while game_while:
        # отрисовать бг
        screen.blit(bg, (0, 0))
        controller.do(snake.direction)
        snake.move(game.game_size)
        UI.draw_snake(snake.snake_list, screen, game.game_size)

        if (Engine.check_collision_with_border(snake, game.screen_size)
                or Engine.check_collision_with_snake(snake)):
            game_while = stop()

        if Engine.check_collision_with_apple(snake.coordinates, apple.coordinates):
            game.score_inc()
            apple.generate_coordinates(game.get_cells(), game.game_size)
            snake.length_inc()

        UI.draw_circle(screen, apple, game.game_size)
        UI.show_score(game.score, screen)

        pygame.display.flip()
        clock.tick(game.speed)


if __name__ == '__main__':
    pygame.init()
    game = create_game()

    #pygame settings
    pygame.display.set_caption('Snake')
    screen = pygame.display.set_mode((game.screen_size.x, game.screen_size.y))
    clock = pygame.time.Clock()
    bg = pygame.image.load('images/background.png').convert()

    #create game objects
    apple = Apple(Apple.get_fruit_coordinates(game.get_cells(), game.game_size))
    controller = Controller()
    snake = create_snake()

    start_game(game=game, screen=screen, controller=controller, snake=snake)