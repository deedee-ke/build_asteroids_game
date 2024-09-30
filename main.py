import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get(): # loop through all events
            if event.type == pygame.QUIT: # if the event is a window close
                return # exit the game loop
            
        screen.fill((0,0,0)) # fill the screen with black(rgb: 0,0,0)
        pygame.display.flip() # refresh the screen

if __name__ == '__main__':
    main()