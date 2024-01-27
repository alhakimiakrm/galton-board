import pygame
import pymunk
import pymunk.pygame_util
from settings import *
from player import Player
from particle import Particle
import level

PLAYER_SPEED = 200
JUMP_IMPULSE = 200

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Scroller")
clock = pygame.time.Clock()

# Pymunk setup
space = pymunk.Space()
space.gravity = GRAVITY
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Game setup
player = Player(space, (WIDTH / 2, HEIGHT / 2))
level.create_ground(space)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Add a particle at the current mouse position
            Particle(space, event.pos)
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move_left(PLAYER_SPEED)
    if keys[pygame.K_d]:
        player.move_right(PLAYER_SPEED)
    if keys[pygame.K_SPACE]:  # Changed from pygame.K_w to pygame.K_SPACE for jump
        player.jump(JUMP_IMPULSE)


    # Game logic goes here

    # Update Pymunk space
    space.step(1 / FPS)

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen with black
    player.draw(screen)
    for shape in space.shapes:
        if isinstance(shape, pymunk.Circle) and shape != player.shape:
            pos = int(shape.body.position.x), int(shape.body.position.y)
            pygame.draw.circle(screen, PARTICLE_COLOR, pos, shape.radius)

    pygame.display.flip()  # Update the display
    clock.tick(FPS)

pygame.quit()
