import pygame, random

passes = 0
amount_of_platforms = 0
scrolling_speed = 3


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, top_or_bottom):
        super().__init__()
        self.top_or_bottom = top_or_bottom
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.moving = False

    def update(self,):
        global passes, amount_of_platforms, scrolling_speed
        if self.moving:
            #if we're not at the end, go forward
            if self.rect.x > -101:
                 self.rect.x -= scrolling_speed
            else:
                #if we're at the end, go back to the start and choose a random hight
                self.rect.x = 641
                if self.top_or_bottom == True:
                    self.rect.y = random.randint(0,200)
                else:
                    self.rect.y = random.randint(260,460)
          
                passes +=1
                amount_of_platforms +=1
            
            
                #after 12 passes we speed up
                if passes > 12:
                    scrolling_speed +=1
                    passes = 0
            