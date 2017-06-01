# Snake Game

import pygame, sys, random, time

""" init pygame and exit if there are errors  """
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!)Had {0} init errors, exiting ... ".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+)PyGame succesfully initialized!")


""" set the main playground """
""" the set_mode expects a tuple """

playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game!")

""" Define Colors"""
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) # snake
black = pygame.Color(0,0,0) # score
white = pygame.Color(255,255,255) # background
brown = pygame.Color(165,42,42) # food

""" FPS (frames per sec controller) """
fpsController = pygame.time.Clock()

""" Important vars """
""" snake start position """
snakePos = [100, 50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpown = True

direction = 'RIGHT'
changeto = direction


""" Game over function """
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    pygame.display.flip()

    time.sleep(4)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit

gameOver()
