import pygame

from .cmd_line import cmd_line
from .pattern import Pattern
from .grid import Board
from .checkerboard import Checkerboard

class Game :

    def __init__(self, width:int, height:int, tile_size:int,fps: int,screen :pygame.Surface,):
        self._width = width
        self._height = height
        self._tile_size = tile_size
        self._fps = fps
        self._screen= screen

        # Pattern from the tx file
        args= cmd_line()
        self._pattern = Pattern.load(args.i)

    def draw_pattern(self):
        """Print the grid with Pygame."""
        for y in range(self._height):
            for x in range(self._width):
                color = (255, 255, 255) if self.pattern._pattern[y, x] == 1 else (0, 0, 0)
                pygame.draw.rect(
                    self._screen, color, 
                    (x * self._tile_size, y * self._tile_size, self._tile_size, self._tile_size)
                )
        pygame.display.flip()
