import pygame as pg
import random
import sys
import time 
from pygame.locals import *

SnakeBody = []
food_x = 15 * random.randint(8, 19)
food_y = 15 * random.randint(8, 19)
width = 405
height = 405
black = (0, 0, 0)
snakehead = {'x': 240, 'y': 120}
SnakeBody.append(snakehead)
move_x = 0
move_y = 15
score=0
CLOCK = pg.time.Clock()
pg.init()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Snake Game")


def food_eaten():
    if snakehead['x'] == food_x and snakehead['y'] == food_y:
        return True
    return False


def gameover():
    if snakehead['x'] >width-15 or snakehead['x'] < 0:
        return True
    if snakehead['y'] >height-15 or snakehead['y'] < 0:
        return True
    for i in range(1, len(SnakeBody)):
        if snakehead['x'] == SnakeBody[i]['x'] and snakehead['y'] == SnakeBody[i]['y']:
            return True
    return False

def display_score():
    global score
    message=str(score) if not gameover() else "Game Over!!!"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (0,0,0))
    screen.fill((255,255,255), (0, 405, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
def move_snake():
    global move_x, move_y, snakehead, score
    new_head = {'x': SnakeBody[0]['x'] + move_x, 'y': SnakeBody[0]['y'] + move_y}
    SnakeBody.insert(0, new_head)
    snakehead=new_head
    if not food_eaten():
        SnakeBody.pop()
    elif food_eaten():
        score+=1
        generate_food()


def update_screen():
    screen.fill(black)
    move_snake()
    display_score()
    for i in SnakeBody:
        head = pg.rect.Rect(i['x'], i['y'], 15, 15)
        pg.draw.rect(screen, (0, 255, 0), head)
    draw_food()

def draw_food():
    food = pg.rect.Rect(food_x, food_y, 15, 15)
    pg.draw.rect(screen, (255, 0, 0), food)


def generate_food():
    global food_x, food_y
    food_x = 15 * random.randint(8, 19)
    food_y = 15 * random.randint(8, 19)


update_screen()
snake_counter=0
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and move_x != 15:
                move_x = -15
                move_y = 0
            elif event.key == K_RIGHT and move_x != -15:
                move_x = 15
                move_y = 0
            elif event.key == K_UP and move_y != 15:
                move_x = 0
                move_y = -15
            elif event.key == K_DOWN and move_y != -15:
                move_x = 0
                move_y = 15
    if not gameover():
        update_screen()
        pg.display.update()
        CLOCK.tick(11)