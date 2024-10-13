class Config:
    WIDTH = 300
    HEIGHT = 600
    GRID_WIDTH = 10
    GRID_HEIGHT = 20
    TILE_SIZE_X = WIDTH // GRID_WIDTH
    TILE_SIZE_Y = HEIGHT // GRID_HEIGHT

    @staticmethod
    def get_colors():
        return [
            (0, 0, 0),  # Чорний (порожній блок)
            (255, 0, 0),  # Червоний
            (0, 255, 0),  # Зелений
            (0, 0, 255),  # Синій
            (255, 255, 0),  # Жовтий
            (255, 165, 0),  # Оранжевий
            (128, 0, 128),  # Фіолетовий
            (0, 255, 255),  # Блакитний
        ]

    @staticmethod
    def get_list_shapes():
        return [
            [[1, 1, 1, 1]],          # Лінія
            [[1, 1],
             [1, 1]],        # Квадрат
            [[0, 1, 0],
             [1, 1, 1]],  # Т
            [[1, 1, 0],
             [0, 1, 1]],  # Z
            [[0, 1, 1],
             [1, 1, 0]],  # S
            [[1, 0, 0],
             [1, 1, 1]],  # L
            [[0, 0, 1],
             [1, 1, 1]],  # J
        ]