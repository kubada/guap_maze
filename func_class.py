from enum import Enum
from typing import Any, List

from pygame import draw

from const import red, cell_size, black, white, green


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


class Maze:
    def __init__(self, maze_width: int, maze_height: int):
        self.width = maze_width
        self.height = maze_height
        self.maze: List[List[int]] = []
        self.end_x: int = 0
        self.end_y: int = 0
        self.density = 0
        self.current_level = 0

        def initialize_maze(self):
            self.maze = [[1] * self.width for _ in range(self.height)]

        def draw(self, screen: Any):
            screen.fill(black)
            for y in range(self.height):
                for x in range(self.width):
                    if self.maze[y][x] == 1:
                        draw.rect(screen, white, (x * cell_size, y * cell_size, cell_size, cell_size))
            draw.rect(screen, green,
                      (self.end_x * cell_size, self.end_y * cell_size, cell_size, cell_size))
