from circleshape import *
from constants import *
from main import *

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