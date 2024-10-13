import pygame

class Controller:
    def __init__(self):
        self._right = True
        self._left = True
        self._up = True
        self._down = False

    def do(self, direction):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.KEYDOWN:
                    self.choose_direction(event, direction)

    def choose_direction(self, event, direction):
        match event.key:
            case pygame.K_LEFT if self.left:
                self.turn_left(direction)
            case pygame.K_RIGHT if self.right:
                self.turn_right(direction)
            case pygame.K_UP if self.up:
                self.turn_up(direction)
            case pygame.K_DOWN if self.down:
                self.turn_down(direction)

    def turn_left(self, direction):
        direction.x = -1
        direction.y = 0
        self.right = False
        self.left = True
        self.up = True
        self.down = True

    def turn_right(self, direction):
        direction.x = 1
        direction.y = 0
        self.right = True
        self.left = False
        self.up = True
        self.down = True

    def turn_up(self, direction):
        direction.x = 0
        direction.y = -1
        self.right = True
        self.left = True
        self.up = True
        self.down = False

    def turn_down(self, direction):
        direction.x = 0
        direction.y = 1
        self.right = True
        self.left = True
        self.up = False
        self.down = True

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def up(self):
        return self._up

    @up.setter
    def up(self, value):
        self._up = value

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value