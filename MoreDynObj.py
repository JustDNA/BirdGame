#Import modules

import pygame, random, sys
from pygame.locals import *
pygame.init()

#intialising variables

window_height=500 
window_width=500

black = (0,0,0)
blue = (0, 0, 225)
fps = 25
font = pygame.font.SysFont(None, 28)
mainClock = pygame.time.Clock()

Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MINI PROJECT')

pygame.display.update()

ballimage = pygame.image.load('ball.png')
ballrect = ballimage.get_rect()



ballrect.centerx = ballrect.centery = 250
speedX = 0
speedY = 0

while True:     # the main game loop
    print(speedX,speedY)
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_UP:
                speedY = speedY - 2
            if event.key == K_DOWN:
                speedY = speedY + 2
            if event.key == K_LEFT:
                speedX = speedX - 2
            if event.key == K_RIGHT:
                speedX = speedX + 2


    if ((ballrect.top > 0) and (ballrect.bottom < 500)):
        ballrect.top += speedY
    else:
        speedY *= -1
        ballrect.top += speedY
    if ((ballrect.left > 0) and (ballrect.right < 500)):
        ballrect.left += speedX
    else:
        speedX *= -1
        ballrect.left += speedX

    print(ballrect.left,ballrect.top,ballrect.right,ballrect.bottom)
    #getting the position of the ball

    x = str(ballrect.centerx)
    y = str(ballrect.centery)

    pos_x = font.render(x, 1, blue)
    pos_y = font.render(y, 1, blue)

    pos_xrect = pos_x.get_rect()
    pos_yrect = pos_y.get_rect()

    pos_xrect.topleft = (10, 10)
    pos_yrect.topleft = (50, 10)


    Canvas.fill(black)
    Canvas.blit(pos_x, pos_xrect)
    Canvas.blit(pos_y, pos_yrect)

    Canvas.blit(ballimage, ballrect)
    pygame.display.update()

    mainClock.tick(fps)

pygame.display.update()
