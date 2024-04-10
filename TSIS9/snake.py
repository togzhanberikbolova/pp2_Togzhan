import pygame
import random
import time

pygame.init()

SCREEN_W = 500
SCREEN_H = 400
snake_speed = 10

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((SCREEN_W, SCREEN_H))


clock = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]


direction = 'RIGHT'
change_to = direction

score = 0

class Food:
    def __init__(self):
        self.position = [random.randrange(1, (SCREEN_W// 10)) * 10,
                         random.randrange(1, (SCREEN_H // 10)) * 10]
        self.spawn_time = pygame.time.get_ticks()
        self.color = red if random.randint(0, 1) == 0 else green  
        self.score = 1 if self.color == white else 2 
        self.duration = 5000  

food = Food()

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_W / 2, SCREEN_H / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food.position[0] and snake_position[1] == food.position[1]:
        score += food.score
        food = Food()
    else:
        snake_body.pop()

    if pygame.time.get_ticks() - food.spawn_time > food.duration:
        food = Food()


    game_window.fill(white)
    for pos in snake_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, food.color, pygame.Rect(food.position[0], food.position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > SCREEN_W-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_H-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    show_score(black, 'times new roman', 20)

    pygame.display.update()

    clock.tick(snake_speed)