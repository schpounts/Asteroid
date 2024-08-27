
import pygame
from constants import *
from player import *

def main():


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_player = Player(INITIAL_X,INITIAL_Y)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(game_player)
    drawable.add(game_player)
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return            
        
        screen.fill("black")


        for obj in updatable:
            obj.update(dt)
        
        

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) /1000
       



if __name__ == "__main__":
    main()