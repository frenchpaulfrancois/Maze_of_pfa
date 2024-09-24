import pygame
import random

class Maze:
    """
    Class to generate and display a maze using Pygame.

    Attributes:
    - width: int
        The width of the maze.
    - height: int
        The height of the maze.
    - maze: list
        A 2D list representing the maze structure.
    """

    def __init__(self, width: int, height: int):
        """
        Initializes the Maze class with specified width and height.

        Parameters:
        - width: int
            The width of the maze.
        - height: int
            The height of the maze.

        Raises:
        - ValueError:
            If width or height is less than 1.
        """

        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")

        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        self.generate_maze(0, 0)

    def generate_maze(self, x: int, y: int):
        """
        Generates the maze using recursive backtracking.

        Parameters:
        - x: int
            The current x position in the maze.
        - y: int
            The current y position in the maze.
        """

        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                self.maze[y + dy // 2][x + dx // 2] = 0
                self.maze[ny][nx] = 0
                self.generate_maze(nx, ny)

    def draw_maze(self):
        """
        Draws the maze using Pygame.
        """

        pygame.init()
        cell_size = 20
        screen_width = self.width * cell_size
        screen_height = self.height * cell_size
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Horrible Maze fro me!")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            for y in range(self.height):
                for x in range(self.width):
                    color = (0, 0, 0) if self.maze[y][x] == 0 else (255, 255, 255)
                    pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

            pygame.display.flip()

        pygame.quit()


# Unit tests for Maze class.

import unittest

class TestMaze(unittest.TestCase):

    def test_valid_maze_initialization(self):
        """
        #Tests if a maze can be initialized with valid dimensions.
        """
        maze = Maze(5, 5)
        self.assertEqual(maze.width, 5)
        self.assertEqual(maze.height, 5)
        self.assertEqual(len(maze.maze), 5)
        self.assertTrue(all(len(row) == 5 for row in maze.maze))

    def test_invalid_maze_initialization_zero_width(self):
        """
        #Tests if ValueError is raised when width is set to zero.
        """
        with self.assertRaises(ValueError):
            Maze(0, 5)

    def test_invalid_maze_initialization_zero_height(self):
        """
        #Tests if ValueError is raised when height is set to zero.
        """
        with self.assertRaises(ValueError):
            Maze(5, 0)

    def test_invalid_maze_initialization_negative_dimensions(self):
        """
        #Tests if ValueError is raised when negative dimensions are provided.
        """
        with self.assertRaises(ValueError):
            Maze(-1, -1)

    def test_maze_structure(self):
        """
        #Tests if the maze structure is generated correctly.
        """
        maze = Maze(5, 5)
        self.assertIn(0, [cell for row in maze.maze for cell in row])
        self.assertIn(1, [cell for row in maze.maze for cell in row])

# usage of the Maze class:



a : int = int(input('maze - length : \n'))
b : int = int(input('maze - width : \n'))
if __name__ == "__main__":
    maze = Maze(a, b)
    maze.draw_maze()
