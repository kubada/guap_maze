from enum import Enum
from typing import Any

from pygame import draw

from const import red, cell_size


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self, screen: Any):
        draw.rect(screen, red, (self.x * cell_size, self.y * cell_size, cell_size, cell_size))
