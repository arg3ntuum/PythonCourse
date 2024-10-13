class Snake:
    def __init__(self, head: [int, int],
                 coordinates, length,
                 snake_list, direction):
        self._head = head
        self._coordinates = coordinates
        self._length = length
        self._snake_list = snake_list
        self._direction = direction

    def move(self, game_size):
        self.coordinates.x += self.direction.x * game_size
        self.coordinates.y += self.direction.y * game_size

        self.head = [self.coordinates.x, self.coordinates.y]
        self.snake_list.append(self.head)

        if len(self.snake_list) > self.length:
            del self.snake_list[0]

    def length_inc(self):
        self._length += 1

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    @property
    def length(self):
        return self._length

    @length.setter
    def snake_length(self, value):
        self._length = value

    @property
    def snake_list(self):
        return self._snake_list

    @snake_list.setter
    def snake_list(self, value):
        self._snake_list = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value