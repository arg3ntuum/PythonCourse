import random
from points import Point


class Apple:

    def __init__(self, coordinates: Point):
        self._coordinates = coordinates

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    def generate_coordinates(self, cells: Point, game_size: int):
        self.coordinates = self.get_fruit_coordinates(cells, game_size)

    @classmethod
    def get_fruit_coordinates(cls, cells: Point, game_size: int) -> Point:
        return Point(random.randrange(1, cells.x) * game_size,
                     random.randrange(1, cells.y) * game_size)