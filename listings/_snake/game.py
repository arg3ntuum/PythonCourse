from _snake import Point, Snake


class Game:
    def __init__(self, screen_size, score = 0,
                 speed = 10, game_size = 15):
        self._screen_size = screen_size
        self._score = score
        self._speed = speed
        self._game_size = game_size

    def score_inc(self):
        self.score += 1

    # розрахунку кількості "клітинок"
    def get_cells(self) -> Point:
        return Point(int(self.screen_size.x / self.game_size),
                     int(self.screen_size.y / self.game_size))

    #розрахунок координат
    def get_coordinates(self, cells: Point) -> Point:
        return Point(int(cells.x / 2) * self.game_size,
                     int(cells.y / 2) * self.game_size)

    @property
    def screen_size(self):
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value):
        self._screen_size = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def game_size(self):
        return self._game_size

    @game_size.setter
    def game_size(self, value):
        self._game_size = value