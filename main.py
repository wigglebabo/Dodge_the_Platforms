import pygame, time, random

# Global constants
GRAVITY = 0.3
JUMP_VELOCITY = -5
FRICTION = 0.9
ACCELERATION = 0.5

# Global vars
scrolling_speed = 2
first_input = False
running = True
passes = 0
amount_of_platforms = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        if first_input:
            # make sure the phisics work
            self.rect.y += self.y_velocity
            self.rect.x += self.x_velocity
            self.y_velocity += GRAVITY
            self.x_velocity *= FRICTION
        #if we're at the top of the screen, send us back down so we don't go over the top
        if self.rect.y <= 0:
            self.y_velocity = 1
        #if we're under the screen we lose
        if self.rect.y > 480:
            global running
            running = False

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        #use global variables
        global passes, amount_of_platforms, scrolling_speed
        #if we're not at the end, go forward
        if self.rect.x > -101:
            self.rect.x -= scrolling_speed
        else:
            #if we're at the end, go back to the start and choose a random hight
            self.rect.x = 641
            self.rect.y = random.randint(0,480)
            passes +=1
            amount_of_platforms +=1
            update_score()
            #after 10 passes we speed up
            if passes > 15:
                scrolling_speed +=1
                passes = 0
            # after 5 platforms we send one at the x-value of the start of the player so he can't stay in one place
            if amount_of_platforms == 5:
                self.rect.y = 300
        

def update_score():
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render(f'score: {amount_of_platforms}', False, (0, 0, 0))
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

platform = Platform(185, random.randint(0,250), 100, 20)
platform_group.add(platform)

platform1 = Platform(370, random.randint(0,250), 100, 20)
platform_group.add(platform1)

platform2 = Platform(555, random.randint(0,250), 100, 20)
platform_group.add(platform2)

platform3 = Platform(740, random.randint(0,250), 100, 20)
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
                first_input = True
                player.y_velocity = JUMP_VELOCITY
            #if we press left we go left
            if event.key == pygame.K_LEFT:
                first_input = True
                player_movement = -1
            #if we press right we go right
            elif event.key == pygame.K_RIGHT:
                first_input = True
                player_movement = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_movement = 0

    player.x_velocity += player_movement * ACCELERATION
    #update everything
    screen.fill((255, 255, 255))
    player_group.update()
    platform_group.update()
    update_score()
    #get collision, if we collide we lose
    collided_sprites = pygame.sprite.spritecollide(player, platform_group, False)
    if collided_sprites:
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