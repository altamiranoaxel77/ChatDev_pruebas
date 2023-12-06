'''
Main file for Snake Game
'''
import pygame
import sys
from pygame.locals import *
from game import Game
def main():
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_RETURN:
                    game.start_game()
                elif event.key == K_m:
                    game.is_in_menu = True
        game.update()
        game.draw()
        pygame.display.update()
        clock.tick(10)
if __name__ == '__main__':
    main()