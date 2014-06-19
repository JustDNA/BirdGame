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
speed = 10
font = pygame.font.SysFont(None, 28)
mainClock = pygame.time.Clock()

Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MINI PROJECT')

pygame.display.update()

ballimage = pygame.image.load('ball.png')
ballrect = ballimage.get_rect()



moveup = movedown = moveright = moveleft = False
ballrect.centerx = ballrect.centery = 250

while True:     # the main game loop

    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_UP:
                if(moveup == True):
                    moveleft = moveright = False
                moveup = True
                movedown = False
            if event.key == K_DOWN:
                if(movedown == True):
                    moveleft = moveright = False
                movedown = True
                moveup = False
            if event.key == K_LEFT:
                if(moveleft == True):
                    moveup = movedown = False
                moveleft = True
                moveright = False
            if event.key == K_RIGHT:
                if(moveright == True):
                    moveup = movedown = False
                moveright = True
                moveleft = False


    if (moveup and (ballrect.top > 0)):
        ballrect.top-= speed
    elif(moveup):
        movedown = True
        moveup = False
    if (movedown and (ballrect.bottom < 500)):
        ballrect.bottom += speed
    elif(movedown):
        movedown = False
        moveup = True
    if (moveleft and (ballrect.left > 0)):
        ballrect.left -= speed
    elif(moveleft):
        moveright = True
        moveleft = False
    if (moveright and (ballrect.right < 500)):
            ballrect.right += speed
    elif(moveright):
        moveright = False
        moveleft = True

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

    pygame.draw.rect(Canvas, blue, (90 , 90, 120, 120), 2)
    Canvas.blit(ballimage, ballrect)
    pygame.display.update()

    mainClock.tick(fps)

pygame.mixer.music.stop()
pygame.display.update()
