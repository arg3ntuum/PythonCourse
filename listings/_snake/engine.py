from _snake.points import Point
from _snake.snake import Snake
class Engine:
    def __init__(self):
        pass

    @staticmethod
    def check_collision_with_apple(snake_coord: Point, apple_coord: Point) -> bool:
        if (snake_coord.x == apple_coord.x
                and snake_coord.y == apple_coord.y):
            return True
        return False

    @staticmethod
    def check_collision_with_border(snake: Snake, screen_size) -> bool:
        if (snake.coordinates.x >= screen_size.x
                or snake.coordinates.x < 0
                or snake.coordinates.y >= screen_size.y
                or snake.coordinates.y < 0):
            return True
        return False

    @staticmethod
    def check_collision_with_snake(snake: Snake) -> bool:
        for block in snake.snake_list[:-1]:
            if block == snake.head:
                return True
        return False