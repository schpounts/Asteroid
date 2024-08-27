
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable,drawable)
    
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

        for obj in asteroids:
            if obj.check_collision(game_player):
                print ("Game over!")
                return
        
        for obj in asteroids:
            for bullet in shots:
                if obj.check_collision(bullet):
                    obj.kill()
                    bullet.kill()
                    obj.split()
        
        
        


        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) /1000
       



if __name__ == "__main__":
    main()