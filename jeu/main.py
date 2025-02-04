import pygame
from .cmd_line import cmd_line
from .pattern import Pattern
from .game import Game
def main():

    pygame.init()

    

    clock = pygame.time.Clock()
    args= cmd_line()
    pattern=Pattern.load(args.input_file)
    screen=pygame.display.set_mode( (args.width, args.height) )
    screen.fill( (254, 53, 117 ))
    game= Game(cell_size = args.cell_size,screen=screen, pattern =pattern)

    while args.d:

        clock.tick(args.fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                args.d = False
        game.update()  # Met à jour la grille
        game.draw_pattern()
        

        pygame.display.update()
    
    pygame.quit()

    