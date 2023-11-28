import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920, 1080)) 
pygame.display.set_caption('Asphalt Escapade')                  # initialize pygame, set caption and window
clock = pygame.time.Clock()

backdrop = pygame.image.load('asphalt-escapade/backdrops/city.png').convert_alpha()
backdrop = pygame.transform.scale(backdrop, (1920, 1080))

low_level_enemy = pygame.image.load('asphalt-escapade/characters/l1.png').convert_alpha()
low_level_enemy = pygame.transform.scale(low_level_enemy, (350, 400))
low_level_enemy_original = low_level_enemy
low_level_enemy_rect = low_level_enemy.get_rect(bottomright = (1500, 1100))
low_level_enemy_x = 1200                                                                    #low level enemy initialization
low_level_enemy_y = 750
enemy_speed = 6
enemy_direction = -1

rex = pygame.image.load('asphalt-escapade/characters/rex.png').convert_alpha()
rex = pygame.transform.scale(rex, (250, 250))
rex_rect = rex.get_rect(topleft = (550, 800))
rex_speed = 5                                                                           #main playable character initialization 
move_left = move_right = move_up = move_down = False
rex_original = rex
rex_facing_right = True 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                                   #main loop, exit init
            exit()
           
           #------------------------------------------- 
        elif event.type == pygame.KEYDOWN:              
            if event.key == pygame.K_a:
                move_left = True
                if rex_facing_right:
                    rex = pygame.transform.flip(rex_original, True, False)
                    rex_original = rex
                    rex_facing_right = False                                                            
            elif event.key == pygame.K_d:
                move_right = True                                                           #movement 
                if not rex_facing_right:
                    rex = pygame.transform.flip(rex_original, True, False)
                    rex_original = rex
                    rex_facing_right = True                       
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False             
    if move_right:
        rex_rect.x += rex_speed
    if move_left:
        rex_rect.x -= rex_speed
        #----------------------------------------------------        
        
    
    screen.blit(backdrop, (0, 0))
    low_level_enemy_x += enemy_speed * enemy_direction
    if low_level_enemy_x <= 800 or low_level_enemy_x >= 1200:
        enemy_direction *= -1                                                                       #enemy movement and logic
        low_level_enemy = pygame.transform.flip(low_level_enemy_original, True, False)
        low_level_enemy_original = low_level_enemy
        
    print(rex_rect.colliderect(low_level_enemy_rect))
    
    #playable character blit
    screen.blit(low_level_enemy, low_level_enemy_rect)
    screen.blit(rex, rex_rect)
    
    pygame.display.update()
    clock.tick(60)

