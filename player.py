import pygame



class Player(pygame.sprite.Sprite):
    global first_input, GRAVITY
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((104,245,236))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 0
        self.x_velocity = 0
        self.moving = False

    def update(self, GRAVITY):
        if self.moving:
              # make sure the phisics work
            self.rect.y += self.y_velocity
            self.rect.x += self.x_velocity
            self.y_velocity += GRAVITY

        #if we're at the top of the screen, send us back down so we don't go over the top
        if self.rect.y <= 0:
              self.y_velocity = 1