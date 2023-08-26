from typing import List, Dict

import pygame

from func_class import Player, Maze
from const import width, height, cell_size, black, white


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

    clock = pygame.time.Clock()
    speed = 50

    running = True
    last_move_time = pygame.time.get_ticks()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button_rect.collidepoint(event.pos):
                    maze.reset_maze()
                    player.reset_player(1, 1)
                    running = True  # Сбрасываем флаг на True при нажатии кнопки Reset

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_move_time

        if elapsed_time >= 1000 / speed:
            last_move_time = current_time
            keys = pygame.key.get_pressed()
            dx = 0
            dy = 0
            if keys[pygame.K_UP]:
                dy = -1
            elif keys[pygame.K_DOWN]:
                dy = 1
            elif keys[pygame.K_LEFT]:
                dx = -1
            elif keys[pygame.K_RIGHT]:
                dx = 1

            new_x = player.x + dx
            new_y = player.y + dy

            if len(maze.maze[0]) > new_x >= 0 == maze.maze[new_y][new_x] and 0 <= new_y < len(maze.maze):
                player.x = new_x
                player.y = new_y

        # Проверяем условия завершения игры
        if player.x == maze.end_x and player.y == maze.end_y:
            if maze.current_level < len(levels) - 1:
                maze.current_level += 1
                maze.generate_maze(levels[maze.current_level]['density'], maze.current_level)
                player.reset_player(1, 1)
            else:
                running = False

        screen.fill(black)
        maze.draw_maze(screen)
        player.draw_player(screen)

        pygame.draw.rect(screen, white, reset_button_rect)
        screen.blit(reset_text, (width - 90, height - 45))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
