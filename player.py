from circleshape import *
from constants import *
from main import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = tuple(self.position + forward * self.radius)
        b = tuple(self.position - forward * self.radius - right)
        c = tuple(self.position - forward * self.radius + right)
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt=0):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt=0):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(0-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(0-dt)
       








