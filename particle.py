import pygame
import pymunk

class Particle:
    def __init__(self, space, pos):
        # For a dynamic body, just set the mass and moment without using infinite values.
        mass = 1
        radius = 5
        moment = pymunk.moment_for_circle(mass, 0, radius)  # Calculate moment for a solid circle
        self.body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density = 1  # Optionally set density if required
        self.shape.elasticity = 0.6
        space.add(self.body, self.shape)

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, (255, 255, 0), pos, self.shape.radius)

