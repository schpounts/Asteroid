from circleshape import *
from constants import *
from main import *
import random

class Asteroid(CircleShape): 
    containers = []
    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle( screen, "white",self.position, self.radius, 2)

    def move(self,velocity, dt=0):        
        self.position += velocity * dt


    def update(self, dt):
        self.move(self.velocity,dt)

    def split(self):
        self.kill()        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0,50.0)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2