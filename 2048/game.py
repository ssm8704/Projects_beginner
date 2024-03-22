import mainpage as mp
import pygame as pg
import sys
import time
from pygame.locals import *
width=400
height=400
black=(0,0,0)
line_color=(255,255,255)
num_col=[(255, 0, 0),
(0, 255, 0),
(0, 0, 255),
(255, 255, 0),
(255, 165, 0),
(255, 192, 203),
(0, 255, 255),
(128, 0, 128),
(255, 255, 255),
(128, 128, 128)]
go=None
pg.init()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("2048 game")
initiating_window = pg.image.load("2048game.png")
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
def game_initiating_window():
 
    # displaying over the screen
    screen.blit(initiating_window, (0, 0))
 
    # updating the display
    pg.display.update()
    time.sleep(1)
    screen.fill(color=(0,0,0))
 
def check_pow(val):
    p=0
    while 2**(p+1)!=val:
        p+=1
    return p
    
mp.rangen(0)
def drawnum(row, col, val):
    posx = col * width / 4 + width / 8
    posy = row * height / 4 + height / 8
    c=check_pow(val)
    font = pg.font.Font(None, 50)
    text = font.render(str(mp.r1[row][col]), 1, num_col[c])
    text_rect = text.get_rect(center=(posx, posy))
    screen.blit(text, text_rect)
def update_panel():
    screen.fill(black)  # Clear the screen
    pg.draw.line(screen, line_color, (width / 4, 0), (width / 4, height), 7)
    pg.draw.line(screen, line_color, (width / 4 * 2, 0),(width / 4 * 2, height), 7)
    pg.draw.line(screen, line_color, (width / 4 * 3, 0),(width / 4 * 3, height), 7)
 
    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 4), (width, height / 4), 7)
    pg.draw.line(screen, line_color, (0, height / 4 * 2),(width, height / 4 * 2), 7)
    pg.draw.line(screen, line_color, (0, height / 4 * 3),(width, height / 4 * 3), 7)
    draw_status()
    for i in range(4):
        for j in range(4):
            if mp.r1[i][j] != '':
                drawnum(i, j, mp.r1[i][j])

def draw_status():
    f1=open("score.txt",'r')
    if mp.isover():
        
        message="Game Over!!!"+"            Score:"+str(mp.Score.s)
        if(int(f1.read()))<mp.Score.s:
            f2=open("score.txt",'w')
            f2.write(str(mp.Score.s))
        pg.quit()
    elif mp.iswon():
        message="You Won!!!"
        if(int(f1.read()))<mp.Score.s:
            f2=open("score.txt",'w')
            f2.write(str(mp.Score.s))
        pg.quit()
    else:
        message=str(mp.Score.s)+f"          HI:{f1.read()}"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (0,0,0))
    screen.fill((255,255,255), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
game_initiating_window()
update_panel()
pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mp.adder(mp.r1,'r',-1)
                mp.mover(mp.r1,'r',-1)
                mp.rangen(1)
                update_panel()
                pg.display.update()
            elif event.key == K_RIGHT:
                mp.adder(mp.r1,'r',1)
                mp.mover(mp.r1,'r',1)
                mp.rangen(1)
                update_panel()
                pg.display.update()
            elif event.key == K_UP:
                mp.adder(mp.r1,'c',-1)
                mp.mover(mp.r1,'c',-1)
                mp.rangen(1)
                update_panel()
                pg.display.update()
            elif event.key == K_DOWN:
                mp.adder(mp.r1,'c',1)
                mp.mover(mp.r1,'c',1)
                mp.rangen(1)
                update_panel()
                pg.display.update()
