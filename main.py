import pygame
from time import sleep
from random import randint
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)
PINK = (255, 20, 147)
pygame.init()
colors = [RED,GREEN,BLUE,ORANGE,YELLOW]

theme = 'dark'
hide_score = False
score_plus = False
score1 = 0
score2 = 0
speed_score = -5
speed_score2 = -5
platform_speed = 10
win_score = 20
win_score_show = win_score
start = 0
dx = 5
dy = 5
stop=True
stop2=True
game = True
p=True
qwe=True

if theme == 'dark':
    background = BLACK
    platform_png = "645796b719221c.png"
    ball_png = "645796badfa61c.png"
    score_color = WHITE
    win_score_color = WHITE
if theme == 'white':
    background = WHITE
    platform_png = "645796b719221.png"
    ball_png = "ball_1615463127.png"
    score_color = BLACK
    win_score_color = BLACK

mw = pygame.display.set_mode((500, 500))
mw.fill(background)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = background
        if color:
            self.fill_color = color


    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(x, y)

    


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, width=10, height=10):
        super().__init__(x=x, y=y, width=width,height=height,color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))




ball = Picture(ball_png, 160, 200, 50, 50)
platform1 = Picture(platform_png, 160, 300, 100, 30)
platform2 = Picture(platform_png, 240, 50, 100, 30)
start_x = 5
start_y = 5



for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)


score1s = Label(450,100,50,50)
score2s = Label(450,150,50,50)

ball.fill()
platform1.fill()
platform2.fill()

start_text = Label(150,250,200,25)
start_text.set_text("Press SPACE to start", 30, RED)
set_white = Label(150,300,230,25)
set_white.set_text("Press G to chose theme", 30, WHITE)
set_dark = Label(150,320,230,25)
set_dark.set_text("Press F to chose theme", 30, BLACK)
win_score_text = Label(170,150,200,25)
win_score_text.set_text(win_score_show,30,win_score_color)

move_right1 = False
move_left1 = False

move_right2 = False
move_left2 = False

while game:
    start_text.fill()
    start_text.draw()    
    while p:
        sleep(0.2)
        if win_score>-1:
            win_score_show = win_score
        else:
            win_score_show = "Endless"
        start_text.color(background)
        set_dark.color(background)
        set_white.color(background)
        win_score_text.color(background)
        start_text.fill()
        set_white.fill()
        set_dark.fill()
        win_score_text.fill()
        mw.fill(background)
        start_text.set_text("Press SPACE to start", 30, colors[randint(0,4)])
        win_score_text.set_text("Score to win "+str(win_score_show),30,win_score_color)
        start_text.draw()
        set_white.draw()
        set_dark.draw()
        win_score_text.draw()
        pygame.display.update()
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_text.fill()
                    p=False
                if event.key == pygame.K_f:
                    theme='dark'
                if event.key == pygame.K_g:
                    theme='white'
                if event.key == pygame.K_RIGHT:
                    if win_score != -1:
                        win_score+=1
                    else:
                        win_score+=2
                if event.key == pygame.K_LEFT:
                    if win_score != 1:
                        win_score-=1
                    else:
                        win_score-=2
        if theme == 'dark':
            background = BLACK
            platform_png = "645796b719221c.png"
            ball_png = "645796badfa61c.png"
            score_color = WHITE
            win_score_color = WHITE
        if theme == 'white':
            background = WHITE
            platform_png = "645796b719221.png"
            ball_png = "ball_1615463127.png"
            score_color = BLACK
            win_score_color = BLACK
        if hide_score:
            score_color = background
    if qwe:
        ball = Picture(ball_png, 160, 200, 50, 50)
        platform1 = Picture(platform_png, 160, 300, 100, 30)
        platform2 = Picture(platform_png, 240, 50, 100, 30)
        qwe = False  
    ball.fill()
    platform1.fill()
    platform2.fill()     
    ball.color(background)
    platform1.color(background)
    platform2.color(background)
    score1s.color(background)
    score2s.color(background)
    start_text.color(background)               
    start_text.fill()
    set_white.fill()
    set_dark.fill()
    win_score_text.fill()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right1 = True
            if event.key == pygame.K_LEFT:
                move_left1 = True
        else:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right1 = False
                if event.key == pygame.K_LEFT:
                    move_left1 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right2 = True
            if event.key == pygame.K_a:
                move_left2 = True
        else:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    move_right2 = False
                if event.key == pygame.K_a:
                    move_left2 = False
    if platform1.rect.x >400:
        move_right1 = False
    if platform1.rect.x <0:
        move_left1 = False
    if platform2.rect.x >400:
        move_right2 = False
    if platform2.rect.x <0:
        move_left2 = False
    if move_right1:
        platform1.rect.x += platform_speed
    if move_left1:
        platform1.rect.x -= platform_speed
    if move_right2:
        platform2.rect.x += platform_speed
    if move_left2:
        platform2.rect.x -= platform_speed
    ball.rect.x += dx
    ball.rect.y += dy
    if ball.rect.colliderect(platform1.rect):
        ball.rect.y = 251
        dy *= -1
        if score_plus:
            score2+=1
        uou = True
    if ball.rect.colliderect(platform2.rect):
        ball.rect.y = 77
        dy *= -1
        if score_plus:
            score1+=1
        uou = True
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 350:
        if uou:
            score1+=1
            uou = False
        ball.rect.y = 160
        ball.rect.x = 200
    if ball.rect.y < -50:
        if uou:
            score2+=1
            uou = False
        ball.rect.y = 160
        ball.rect.x = 200
    score1s.set_text(score1, 30, score_color)
    score2s.set_text(score2, 30, score_color)
    if score1 == speed_score or score2 == speed_score:
        if stop:
            dy*=2
            dx*=2
            stop = False
    if score1 == speed_score2 or score2 == speed_score2:
        if stop2:
            dy*=2
            dx*=2
            platform_speed *=1.5
            stop2 = False
    if score1==win_score:
        lose = Label(150,200,10,10)
        lose.set_text("2 win", 50, GREEN)
        lose.draw()
        score1s.set_text(score1, 30, GREEN)
        score1s.draw()
        score2s.draw()
        game = False
    if score2==win_score:
        lose = Label(150,200,10,10)
        lose.set_text("1 win", 50, GREEN)
        lose.draw()
        score2s.set_text(score2, 30, GREEN)
        score1s.draw()
        score2s.draw()
        game = False
    score1s.draw()
    score2s.draw()
    platform1.draw()
    platform2.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(60)

