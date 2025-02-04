import pygame
from .cmd_line import cmd_line
from .pattern import Pattern

def main():

    pygame.init()

    screen = pygame.display.set_mode( (600, 400) )

    clock = pygame.time.Clock()
    args= cmd_line()

    while args.d:

        clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                args.d = False
                
        self.grid.update()  # Met à jour la grille
        self.draw_grid()
        screen.fill( (255 ,255, 255) )

        pygame.display.update()
    
    pygame.quit()

    