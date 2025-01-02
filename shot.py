from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="#ffffff", radius=self.radius, width=1, center=self.position)

    def update(self, dt):
        self.position += (self.velocity*dt)