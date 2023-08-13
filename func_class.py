__author__ = 'Danil A. Kuba'
__copyright__ = 'Copyright 2023, Danil A. Kuba'
__email__ = 'd@kubada.ru'

from enum import Enum
from random import choice, randrange
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

    def move_player(self, direction: Direction, maze: List[List[int]]):
        dx, dy = direction.value
        if maze[self.y + dy][self.x + dx] == 0:
            self.x += dx
            self.y += dy

    def reset_player(self, x, y):
        self.x = x
        self.y = y

    def draw_player(self, screen: Any):
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

    def generate_maze(self, density: int, current_level: int):
        self.initialize_maze()
        self.density = density
        self.current_level = current_level

        self.maze = [[1] * self.width for _ in range(self.height)]

        for y in range(1, self.height - 1, 2):
            for x in range(1, self.width - 1, 2):
                self.maze[y][x] = 0

                adjusted_density = density - (current_level * 2)
                for _ in range(adjusted_density):
                    dx, dy = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                    nx, ny = x + dx, y + dy

                    if self.width > nx >= 0 != self.maze[ny][nx] and 0 <= ny < self.height:
                        self.maze[ny][nx] = 0

        self.end_x = randrange(1, self.width - 1, 2)
        self.end_y = randrange(1, self.height - 1, 2)
        self.maze[self.end_y][self.end_x] = 0

        self.carve_paths(self.end_x, self.end_y)

    def reset_maze(self):
        self.initialize_maze()
        self.generate_maze(self.density, self.current_level)

    def carve_paths(self, x: int, y: int):
        self.maze[y][x] = 0

        for _ in range(4):
            dx, dy = choice([(0, 2), (0, -2), (2, 0), (-2, 0)])
            nx, ny = x + dx, y + dy

            if self.width > nx >= 0 != self.maze[ny][nx] and 0 <= ny < self.height:
                self.maze[y + dy // 2][x + dx // 2] = 0
                self.carve_paths(nx, ny)

    def draw(self, screen: Any):
        screen.fill(black)
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 1:
                    draw.rect(screen, white, (x * cell_size, y * cell_size, cell_size, cell_size))
        draw.rect(screen, green,
                  (self.end_x * cell_size, self.end_y * cell_size, cell_size, cell_size))
