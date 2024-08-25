
import pygame
from constants import *
from player import *

def main():


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_player = player.player(INITIAL_X,INITIAL_Y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return            
        
        screen.fill("black")
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) /1000
        game_player.draw(screen)



if __name__ == "__main__":
    main()