from typing import List, Dict

import pygame

from const import width, height, cell_size, black, white
from func_class import Player, Maze


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Случайный лабиринт')

    levels: List[Dict[str, int]] = [{'name': 'Easy', 'density': 2}, {'name': 'Medium', 'density': 4},
                                    {'name': 'Hard', 'density': 6}]
    current_level: int = 0

    maze = Maze(width // cell_size, height // cell_size)
    maze.initialize_maze()
    maze.generate_maze(levels[current_level]['density'], current_level)
    player = Player(1, 1)

    reset_button_rect = pygame.Rect(width - 100, height - 50, 80, 30)
    font = pygame.font.Font(None, 24)
    reset_text = font.render('Сброс', True, black)

    screen.fill(black)
    maze.draw(screen)
    player.draw_player(screen)

    pygame.draw.rect(screen, white, reset_button_rect)
    screen.blit(reset_text, (width - 90, height - 45))

    pygame.display.flip()


pygame.quit()

if __name__ == '__main__':
    main()
