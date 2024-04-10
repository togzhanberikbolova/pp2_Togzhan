import pygame 
from pygame.locals import *
import sys
import random,time

pygame.init()
FPS=60
clock=pygame.time.Clock()
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

font= pygame.font.SysFont("VERDANA", 60)
smallfont= pygame.font.SysFont("VERDANA",20)
gameov= font.render("GAME OVER!", True, BLUE)

bg = pygame.image.load("download/track.png")
SCREEN_W = 400
SCREEN_H = 600
speed=5
score=0
count=0
 
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
pygame.display.set_caption("Car racer")
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("download/r2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_W-40),0) 
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top> 600):
            score +=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("download/R.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_W:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        yoyimage = pygame.image.load("download/coin.png")
        self.image = pygame.transform.scale(yoyimage, (45, 45))
        self.rect= self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_W-40),0)
    
    def move(self):
        
        self.rect.move_ip(0,speed)
        if (self.rect.top> 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
         
P1 = Player()
E1 = Enemy()
C1 = coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coinies = pygame.sprite.Group()
coinies.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED,1000)

 
while True:     
    for event in pygame.event.get(): 
        if event.type == INC_SPEED:
            speed+=0.5   

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    screen.blit(bg,(0,0))
    scores= smallfont.render(str(score),True, BLACK)
    counts=smallfont.render(str(count),True,BLACK)
    screen.blit(scores,(10,10))
    screen.blit(counts,(370,10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1,coinies):
       
    
       for bonus in coinies:
           bonus.rect.top =0
           bonus.rect.center = (random.randint(30,370),0)
           count+=1

    pygame.display.flip()

    collision_found = False
    for enemy in enemies:
        if pygame.sprite.spritecollideany(enemy, coinies):
           collision_found = True
           break 

    if not collision_found:
        pass

    if pygame.sprite.spritecollideany(P1,enemies):
        time.sleep(0.5)

        screen.fill(BLACK)
        screen.blit(gameov,(30,250))
    
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
             
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
         
    pygame.display.update()
    clock.tick(FPS)

            