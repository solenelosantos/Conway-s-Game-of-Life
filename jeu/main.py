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

    # Load the initial pattern
    pattern=Pattern.load(args.input_file)

    # Create the screen and launch the game
    screen=pygame.display.set_mode( (args.width, args.height) )
    screen.fill( (255, 255, 255 ))
    game= Game(cell_size = args.cell_size,screen=screen, pattern =pattern)

    # Number of steps to run
    step=0

    while args.d:

        clock.tick(args.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or step>args.m:
                # Save the last pattern
                game.save(args.output_file)
                args.d = False

        # Update the grid
        game.update()
        game.draw_pattern()
        pygame.display.update()

        # Increase the step
        step+=1

    pygame.quit()
