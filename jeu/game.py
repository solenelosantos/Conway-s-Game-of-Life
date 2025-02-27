# Standart
import logging

import pygame

# First party
from .cmd_line import cmd_line
from .pattern import Pattern, logger


class Game :
    """The main class of the game."""

    def __init__(self, cell_size:int,screen: pygame.Surface, pattern: Pattern) -> None:
        """Object initialization."""
        self._cell_size = cell_size
        # Pattern from the tx file
        self._pattern = pattern.get_pattern()

        args=cmd_line()
        self._width= args.width
        self._height= args.height

        self._screen = screen

    def draw_pattern(self) -> None:
        """Print the grid with Pygame."""
        for x in range(100):
            for y in range(100):
                color = (0, 0, 0) if self._pattern[x][y] == 1 else (255,255,255)
                rect = pygame.Rect(y*self._cell_size, x*self._cell_size,
                                   self._cell_size, self._cell_size)
                pygame.draw.rect(
                self._screen, color,
                rect)
        pygame.display.flip()

    def count_neighbors(self, x: int, y: int) -> int:
        """Count the number of cells alive around one cell (8 neighbors)."""
        neighbors = (
            self._pattern[x][y-1]+
            self._pattern[x][y+1]+
            self._pattern[x-1][y-1]+
            self._pattern[x-1][y]+
            self._pattern[x-1][y+1]+
            self._pattern[x+1][y-1]+
            self._pattern[x+1][y]+
            self._pattern[x+1][y+1]
            )
        return neighbors  # noqa: RET504


    def update(self)-> None:
        """Update the grid according to rules of Game of Life."""
        new_pattern = [[self._pattern[x][y] for y in range(100)] for x in range(100)]
        for x in range(1,100-1):
            for y in range(1,100-1):
                alive_neighbors = self.count_neighbors(x, y)
                if self._pattern[x][y] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                    new_pattern[x][y] = 0  # Died by under/overpopulation
                elif self._pattern[x][y] == 0 and alive_neighbors == 3:
                    new_pattern[x][y] = 1  # Born by reproduction
        self._pattern = new_pattern

    def save(self, filename: str= "my_output_file.txt")-> None:
        """Set the path to the output file : the final state of our simulation."""
        logger.setLevel(logging.INFO)
        logger.info("The last path was saved to the outpul file.")
        with open(filename, "w") as f:
            for row in self._pattern:
                f.write("".join(str(cell) for cell in row) + "\n")
