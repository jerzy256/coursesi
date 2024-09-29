import pygame as pg
import sys

BLACK=(255,255,255)
WHITE=(0,0,0)
BLOCK_X = 10
BLOCK_Y = 10
SCREEN_WIDTH=600
SCREEN_HEIGHT=800
screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
Clock=pg.time.Clock()

PLATFORM_WIDTH=200
PLATFORM_HEIGHT=30
PLATFORM_X=(SCREEN_WIDTH+PLATFORM_WIDTH) //2
PLATFORM_Y=int(SCREEN_HEIGHT*0.75)
PLATFORM_SPEED=3
BALL_SPEED=3

FPS=120

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

    keys=pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        PLATFORM_X-=PLATFORM_SPEED
        PLATFORM_X=max(0,PLATFORM_X)
    if keys[pg.K_RIGHT]:
        PLATFORM_X+=PLATFORM_SPEED
        PLATFORM_X=min(SCREEN_WIDTH-PLATFORM_WIDTH,PLATFORM_X)

    BLOCK_Y = BLOCK_Y + BALL_SPEED
    
    screen.fill(WHITE)

    platform=pg.Rect(PLATFORM_X,PLATFORM_Y,PLATFORM_WIDTH,PLATFORM_HEIGHT)
    pg.draw.rect(screen,BLACK,platform)

    cube=pg.Rect(BLOCK_X,BLOCK_Y,100,100)
    pg.draw.rect(screen,BLACK,cube)

    if platform.colliderect(cube):
        BALL_SPEED = -BALL_SPEED
    if BLOCK_Y <= 0 :
        BALL_SPEED = -BALL_SPEED
    if BLOCK_Y + 100 >= SCREEN_HEIGHT :
        BALL_SPEED = -BALL_SPEED

    

    pg.display.flip() 
    Clock.tick(FPS)
