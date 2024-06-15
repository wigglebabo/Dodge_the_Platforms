import pygame, time, random
from  platform import Platform
from player import Player

# Global constants
GRAVITY = 0.3
JUMP_VELOCITY = -6

ACCELERATION = 0.3

# Global vars
scrolling_speed = 2
first_input = False
running = True 

        

def update_score():
    from platform import amount_of_platforms
    
    if amount_of_platforms < 50:
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'score: {amount_of_platforms//2}', False, (255, 100, 100))
        screen.blit(text, (475, 25))
    else:
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'score: {amount_of_platforms//2}', False, (100, 255, 100))
        screen.blit(text, (475, 25))
    

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Create player and platform sprites
player = Player(100, 300)
player_group = pygame.sprite.Group()
player_group.add(player)

#platforms
platform_group = pygame.sprite.Group()

platform = Platform(370, random.randint(0,210), 100, 20, True)
platform_group.add(platform)

platform1 = Platform(370, random.randint(250,460), 100, 20, False)
platform_group.add(platform1)

platform2 = Platform(740, random.randint(0,210), 100, 20, True)
platform_group.add(platform2)

platform3 = Platform(740, random.randint(250,460), 100, 20, False)
platform_group.add(platform3)


#make sure the player isn't moving
player_movement = 0

update_score()

# Main game loop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #if we press space we go up
            if event.key == pygame.K_SPACE:
                player.moving = True
                for platform in platform_group:
                    platform.moving = True
                
                player.y_velocity = JUMP_VELOCITY
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_movement = 0

    player.x_velocity += player_movement * ACCELERATION
    #update everything
    screen.fill((255, 255, 255))
    player_group.update(GRAVITY)
    platform_group.update()
    update_score()
    #get collision, if we collide we lose
    collided_sprites = pygame.sprite.spritecollide(player, platform_group, False)
    if collided_sprites or player.rect.y > 481:
        running = False
    #draw the sprites
    player_group.draw(screen)
    platform_group.draw(screen)
    #update the screen
    pygame.display.flip()
    #use the clock so we don't go too fast (60fps max)
    clock.tick(60)




# end screen
screen.fill((255,255,255))
update_score()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text = font.render('GAME OVER', False, (0, 0, 0))
screen.blit(text, (250, 240))
pygame.display.flip()
time.sleep(3)
pygame.quit()