import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()
W,H = 400,600
screen = pygame.display.set_mode((W,H))

pygame.display.set_caption("Car racer")

bg = pygame.image.load('download/r.png')
car1 = pygame.image.load('download/R1.png')
car2 = pygame.image.load('download/r2.png')

def car(x,y):
    screen.blit(car1, (x,y))
def thing1(x,y):
    screen.blit(car2, (x,y))
thing1_startx = random.randrange(100,500)
thing1_starty = -50
thing1_speed = 3
thing1_width = 2
thing1_height = 5

x_change = 0
x = 100
y = 350

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            runing =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change=-2
            if event.key == pygame.K_RIGHT:
                x_change=2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                x_change = 0
    x+=x_change            
    screen.blit(bg, (0,0))
    thing1(thing1_startx, thing1_starty)
    car(x,y)
    if thing1_starty > H:
        thing1_starty = 0-thing1_height
        thing1_startx = random.randrange(200,585)
    
    thing1_starty += thing1_speed
   
    pygame.display.update()
    clock.tick(60)
                                  