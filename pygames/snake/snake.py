#!/usr/bin/python

import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)

# hold the position of a map block, using the constructor to pass the x and y coordinates
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# gameplay class
class GameData:
    def __init__(self):
        self.lives = 3
        self.isDead = False
        self.blocks = []
        self.tick = 250
        self.speed = 250
        self.level = 1
        self.berrycount = 0
        self.segments = 1
        
        self.frame = 0
        
        bx = random.randint(1, 38)
        by = random.randint(1, 28)
        
        self.berry = Position(bx, by)
        self.blocks.append(Position(20,15))
        self.blocks.append(Position(19,15))
        
        self.direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down

def loseLife(gamedata):
        pass
   
def positionBerry(gamedata):
        pass
    
def loadMapFile(fileName):
    f = open(fileName, 'r')
    content = f.readlines()
    f.close()

    return content
    
def headHitBody(gamedata):
        return False3
    
def headHitWall(map, gamedata):
        return False
    
def drawData(surface, gamedata):
        pass
    
def drawGameOver(surface):
    text1 = font.render("Game Over", 1, (255, 255, 255))
    text2 = font.render("Space to play or close the window",)
    textpos1 = text1.get_rect(centerx=surface.get_width()/2, top=surface.get_height()/2 - 48)
    textpos2 = text2.get_rect(centerx=surface.get_width()/2, top=surface.get_height()/2)

    surface.blit(text1, textpos1)
    surface.blit(text2, textpos2)
    
def drawWalls(surface, img, map):
    row = 0
    for line in map:
        col = 0
        for char in line:
            if( char == '1' ):
                imgRect = img.get_rect()
                imgRect.left = col * 16
                imgRect.top = row * 16
                surface.blit(img, imgRect)
            col += 1
        row += 1
     
def drawSnake(surface, img, gamedata):
        pass
    
def updateGame(gamedata, gameTime):
        pass
    
def loadImages():
    wall = pygame.image.load('assets/wall.png')
    raspberry = pygame.image.load('assets/berry.png')
    snake = pygame.image.load('assets/snake.png')
    return {'wall':wall, 'berry':raspberry, 'snake':snake}


images = loadImages()
images['berry'].set_colorkey((255, 0, 255))

snakemap = loadMapFile('map.txt')
data = GameData()
quitGame = False
isPlaying = False
    
while not quitGame:
    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 28)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16
        rrect.top = data.berry.y * 16


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

                    
    
# update stuff here

isPlaying = (data.lives > 0 )

if (isPlaying):
    surface.fill((0,0,0))
    # do drawing stuff here
    drawWalls(surface, images['wall'], snakemap)
    surface.blit(images['berry'], rrect)

    drawSnake(surface, images['snake'], data)
    sdrawData(surface, data)
    
else:
   keys = pygame.key.get_pressed()
   for event in pygame.event.get():
     if event.type == QUIT:
           pygame.quit()
           sys.exit()

     if (keys[K_SPACE]):
           isPlaying = True
           data = None
           data = GameData()

           drawGameOver(surface)
           pygame.display.update()
           fpsClock.tick(30)
        
