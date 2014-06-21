#Import modules

import pygame, random, sys
from pygame.locals import *
pygame.init()

class rect:
    def __init__(self,a,b):
        self.rand = a
        self.posHor = b
        self.count = 0
    def reset(self):
        self.rand = -1
        self.posHor = 900
        self.count += 1

def drawObs(rect1):
    if(rect1.rand == -1):
        rect1.rand = random.randrange(50, 300)
        rect1.posHor = 900
        pygame.draw.rect(Canvas, blue, (rect1.posHor , 0, 70, rect1.rand), 2)
        pygame.draw.rect(Canvas, blue, (rect1.posHor , rect1.rand+150, 70, 500-rect1.rand-150), 2)
    else:
        if(rect1.posHor - 10 > -70):
            rect1.posHor = rect1.posHor-10
            pygame.draw.rect(Canvas, blue, (rect1.posHor , 0, 70, rect1.rand), 2)
            pygame.draw.rect(Canvas, blue, (rect1.posHor , rect1.rand+150, 70, 500-rect1.rand-150), 2)
        else:
            rect1.reset()


#intialising variables

window_height=500
window_width=900
a = b = 250
black = (0,0,0)
blue = (0, 0, 225)
white = (255,255,255)
fps = 25
font = pygame.font.SysFont(None, 28)
mainClock = pygame.time.Clock()

Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MINI PROJECT')

pygame.display.update()

ballimage = pygame.image.load('bird4.png')
ballrect = ballimage.get_rect()

a = random.randrange(100, 300)
rect1 = rect(a,900)
a = random.randrange(100, 300)
rect2 = rect(a,1200)
a = random.randrange(100, 300)
rect3 = rect(a,1500)

ballrect.centerx = ballrect.centery = 250
speedX = 0
speedY = 0

frameMod = 0

while True:     # the main game loop
    frameMod = frameMod % 25
    if(frameMod % 5 == 0):
        ballimage = pygame.image.load('bird4.png')
        ballrect = ballimage.get_rect()
        ballrect.centerx = a
        ballrect.centery = b

    print(speedX,speedY)
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_UP:
                ballimage = pygame.image.load('bird2.png')
                ballrect = ballimage.get_rect()
                ballrect.centerx = a
                ballrect.centery = b
                Canvas.blit(ballimage, ballrect)
                frameMod = 0
                speedY = speedY - 8
            if event.key == K_DOWN:
                ballimage = pygame.image.load('bird3.png')
                ballrect = ballimage.get_rect()
                ballrect.centerx = a
                ballrect.centery = b
                Canvas.blit(ballimage, ballrect)
                frameMod = 0
                speedY = speedY - 4
                speedY = speedY + 3
            if event.key == K_LEFT:
                speedX = speedX - 2
            if event.key == K_RIGHT:
                speedX = speedX + 2
            if event.key == K_SPACE:
                if speedX>0:
                    speedX -= 2
                elif(speedX!=0):
                    speedX += 2
                if speedY>0:
                    speedY -= 2
                elif(speedY!=0):
                    speedY += 2


    if ((ballrect.top > 0) and (ballrect.bottom < 500)):
        ballrect.top += speedY
    else:
        speedY *= -0.75
        ballrect.top += speedY
    if ((ballrect.left > 0) and (ballrect.right < 900)):
        ballrect.left += speedX
    else:
        speedX *= -0.75
        ballrect.left += speedX

    speedY+=0.3

    print(ballrect.left,ballrect.top,ballrect.right,ballrect.bottom)
    #getting the position of the ball
    a = ballrect.centerx
    b = ballrect.centery
    x = str(ballrect.centerx)
    y = str(ballrect.centery)

    pos_x = font.render(x, 1, blue)
    pos_y = font.render(y, 1, blue)

    pos_xrect = pos_x.get_rect()
    pos_yrect = pos_y.get_rect()

    pos_xrect.topleft = (10, 10)
    pos_yrect.topleft = (50, 10)


    Canvas.fill(white)
    Canvas.blit(pos_x, pos_xrect)
    Canvas.blit(pos_y, pos_yrect)
    drawObs(rect1)
    drawObs(rect2)
    drawObs(rect3)
    Canvas.blit(ballimage, ballrect)
    pygame.display.update()

    mainClock.tick(fps)
    frameMod += 1
pygame.display.update()
