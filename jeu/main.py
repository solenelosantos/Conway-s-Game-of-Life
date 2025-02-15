# Standart
import pygame

# First party
from .cmd_line import cmd_line
from .game import Game
from .pattern import Pattern


def main()-> None:
    """Define the main function of the game."""
    pygame.init()

    clock = pygame.time.Clock()

    args= cmd_line()

    pattern=Pattern.load(args.input_file)
    screen=pygame.display.set_mode( (args.width, args.height) )
    screen.fill( (0, 0, 0 ))

    game= Game(cell_size = args.cell_size,screen=screen, pattern =pattern)
    step=0

    while args.d:

        clock.tick(args.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or step>args.m:
                args.d = False
        # Update the grid
        game.update()
        game.draw_pattern()
        pygame.display.update()
        step+=1

    pygame.quit()