import pygame
import pymunk

class Player:
    def __init__(self, space, pos):
        self.body = pymunk.Body(1, float('inf'))  # Use float('inf') instead of pymunk.inf
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, 15)  # Radius of 15
        self.shape.elasticity = 0.5
        self.shape.friction = 1.0
        space.add(self.body, self.shape)

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, (0, 255, 0), pos, self.shape.radius)


    def move_left(self, speed):
        self.body.velocity = (-speed, self.body.velocity.y)

    def move_right(self, speed):
        self.body.velocity = (speed, self.body.velocity.y)

    def jump(self, impulse):
        # Simple jump implementation; might need refinement for checking if on ground
        if abs(self.body.velocity.y) < 1e-6:  # Roughly checks if the player is not moving vertically
            self.body.apply_impulse_at_local_point((0, -impulse))
            
            