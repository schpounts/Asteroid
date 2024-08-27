
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    game_player = Player(INITIAL_X,INITIAL_Y)
    field_of_asteroid = AsteroidField()

    

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