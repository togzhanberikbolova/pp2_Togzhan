import pygame
from datetime import datetime

pygame.init()
W,H = 600,500
screen = pygame.display.set_mode((W,H))
clock=pygame.time.Clock()

pygame.display.set_caption("Mickey_Clock")
icon = pygame.image.load('download/clock24.png')
pygame.display.set_icon(icon)

clock1 = pygame.image.load('download/mainclock.png')
leftarm = pygame.image.load('download/leftarm.png')
rightarm = pygame.image.load('download/rightarm.png')

clock2 = pygame.transform.scale(clock1,(600,400))
ra = pygame.transform.scale(rightarm,(600,600))
la = pygame.transform.scale(leftarm, (40,450))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
    screen.fill("white")
    mid = clock2.get_rect(center=(W//2, H//2))
    screen.blit(clock2, mid)
    t = datetime.now()
    sec = -(t.second * 6)
    min = -(t.minute * 6 + t.second*0.1)
    
    ra_rot = pygame.transform.rotate(ra, min)
    la_rot = pygame.transform.rotate(la, sec)
    
    ra_mid = ra_rot.get_rect(center= (W//2, H//2))
    la_mid = la_rot.get_rect(center= (W//2, H//2))
    
    screen.blit(ra_rot, ra_mid)
    screen.blit(la_rot, la_mid)
    clock.tick(60)
    
    
    pygame.display.flip()
    pygame.display.update()
            

