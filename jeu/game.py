import pygame
from .pattern import Pattern
from .cmd_line import cmd_line

class Game :

    def __init__(self, cell_size:int,screen: pygame.Surface, pattern: Pattern):
        self._cell_size = cell_size
    

        # Pattern from the tx file
        self._pattern = pattern.get_pattern()

        args=cmd_line()
        self._width= args.width
        self._height= args.height

        self._screen = screen

    def draw_pattern(self):
        """Print the grid with Pygame."""
        for x in range(self._height):
            for y in range(self._width):
                color = (255, 255, 255) if self._pattern[x][y] == 1 else (0,0,0)
                rect = pygame.Rect(y, x, self._cell_size, self._cell_size)
                pygame.draw.rect(
                self._screen, color, 
                rect
                )
                
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
        return neighbors
    
    def update(self):
        """Update the grid according to rules of Game of Life."""
        new_pattern = [[self._pattern[x][y] for y in range(self._width)] for x in range(self._height)]
        for x in range(1,self._height-1):
            for y in range(1,self._width-1):
                alive_neighbors = self.count_neighbors(x, y)
                if self._pattern[x][y] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                    new_pattern[x][y] = 0  # Died by under/overpopulation
                elif self._pattern[x][y] == 0 and alive_neighbors == 3:
                    new_pattern[x][y] = 1  # Born by reproduction            
        self._pattern = new_pattern