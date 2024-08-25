from circleshape import *

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
        







