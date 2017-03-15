import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks')
black = pygame.Color(0, 0, 0)

# bat init
bat = pygame.image.load('assets/bat.png')
playerY = 540
batRect = bat.get_rect()
mousex, mousey = (0, playerY)

# ball init
ball = pygame.image.load('assets/ball.png')
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed = 3
ballServed = False

bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)

# brick init
brick = pygame.image.load('assets/brick.png')
bricks = []

# create the positions of each of the bricks

for y in range(5):
    brickY = ( y * 24 ) + 100
    for x in range(10):
        brickX = ( x * 31 ) + 245
        bricks.append(Rect(brickX, brickY, brick.get_width(),
                                        brick.get_height()))


    
while True:
    # each time the loop is executed we clear the main surface
    mainSurface.fill(black)
    
    # brick draw
    for b in bricks:
        mainSurface.blit(brick, b)
    
    # bat and ball draw
    mainSurface.blit(bat, batRect)

    mainSurface.blit(ball, ballRect)
    
    # events
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if ( mousex < 800 - 55):
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = (800 - 55, playerY)
        elif event.type == MOUSEBUTTONUP:
            if not ballServed:
                ballServed = True
                
    # main game logic
    if ballServed:
        bx += sx
        by += sy
        ballRect.topleft = (bx, by)

    # the top and bottom of the screen will reflect  on the y axis
    # ensure that the topmost boundary of the screen reflets the ball
    if by <= 0:
        by = 0
        sy *= -1
        
    # ensure that teh bottom boundary of the srcreen reflects the ball
    # if ball hits the bottom set it as out of bounds and reset it
    if by >= 600 - 8:
        ballServed = False
        bx, by = (24, ballStartY)
        ballRect.topleft = (bx, by )
        

    # the sides of the screen will reflect on the x axis
    # reflect the ball on the left hand edge
    if bx <= 0:
        bx = 0
        sx *= -1

    # reflect the ball on the right-hand edge
    if bx >= 800 - 8:
        bx = 800 - 8
        sx *= -1

    
    # collision detection
    # bat and ball collision using the collidirect method of the Rect class
    if ballRect.colliderect(batRect):
        by = playerY - 8
        sy *= -1


    # brick and ball collision
    brickHitIndex = ballRect.collidelist(bricks)
    if brickHitIndex >= 0:
        hb = bricks[brickHitIndex]

        mx = bx + 4
        my = by + 4
        if mx > hb.x +hb.width or mx < hb.x:
            sx *= -1
        else:
            sy *= -1

        del(bricks[brickHitIndex])
    
    pygame.display.update()
    
    fpsClock.tick(30)
