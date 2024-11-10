import pygame as pg
import sys
pg.init()
BLACK=(255,255,255)
WHITE=(0,0,0)
BLOCK_X = 10
BLOCK_Y = 10
SCREEN_WIDTH=600
SCREEN_HEIGHT=750
screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
assets = {
    'ball': pg.image.load('ball.png').convert(),
    'background': pg.image.load('background.png').convert(),
    'platform': pg.image.load('panel.png').convert(),
}
Clock=pg.time.Clock()
count = 0
def_font = pg.font.Font(pg.font.get_default_font(), 30)
PLATFORM_WIDTH=200
PLATFORM_HEIGHT=30
PLATFORM_X=(SCREEN_WIDTH+PLATFORM_WIDTH) //2
PLATFORM_Y=int(SCREEN_HEIGHT*0.75)
PLATFORM_SPEED=3
BALL_SPEED=3
DIRECTION = pg.math.Vector2(1.3,1).normalize()
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
    speed_vector = DIRECTION * BALL_SPEED
    BLOCK_Y +=speed_vector.y
    BLOCK_X +=speed_vector.x
    screen.fill(WHITE)
    platform=pg.Rect(PLATFORM_X,PLATFORM_Y,PLATFORM_WIDTH,PLATFORM_HEIGHT)
    pg.draw.rect(screen,BLACK,platform)
    cube = assets['ball'].get_rect()
    cube.x = BLOCK_X
    cube.y = BLOCK_Y
    screen.blit(assets['ball'],cube)
    block_center = (cube.x + cube.width/2,cube.y + cube.height/2  )
    platform_center = (platform.x + platform.width/2,platform.y + platform.height/2)
    text_surfase = def_font.render(str(count),False,(0,255,0))
    if platform.colliderect(cube):
        collision_vector = (block_center[0]-platform_center[0],block_center[1]-platform_center[1])
        DIRECTION = pg.math.Vector2(collision_vector).normalize()
        count = count + 1
    if BLOCK_Y <= 0 :
        DIRECTION = DIRECTION.reflect(pg.math.Vector2(0,1))
    if BLOCK_Y + 100 >= SCREEN_HEIGHT :
        DIRECTION = DIRECTION.reflect(pg.math.Vector2(0,-1))
        sys.exit()
    if BLOCK_X <= 0 :
        DIRECTION = DIRECTION.reflect(pg.math.Vector2(1,0))
    if BLOCK_X + 100 >= SCREEN_WIDTH :
        DIRECTION = DIRECTION.reflect(pg.math.Vector2(-1,0))
    screen.blit(text_surfase,(20,20))
    pg.display.flip() 
    Clock.tick(FPS) 