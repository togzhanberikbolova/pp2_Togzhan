import pygame
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x =50
y =50
r=25
clock=pygame.time.Clock()

def c(v,min_value,max_value):
        return max(min_value,min(v,max_value))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20
        
        screen.fill((255,255,255))
        w,h=screen.get_size()
        x=c(x,r,w-r)
        y=c(y,r,h-r)
        pygame.draw.circle(screen, (255,0,0), (x,y),25,0)
        
        pygame.display.flip()
        clock.tick(60)
pygame.quit()

     
                
                
            