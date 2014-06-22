#Import modules

import pygame, random, sys
from pygame.locals import *
pygame.init()

class rect:
    def __init__(self,a,b):
        self.rand = a
        self.posHor = b
        self.count = 0
        self.left = -1
        self.top = -1
        self.right = -1
        self.food = -1
        self.foodLeft = -1
        self.foodTop = -1
        self.foodRight = -1
    def reset(self):
        self.rand = -1
        self.posHor = 900
        self.count += 1
        self.left = -1
        self.top = -1
        self.right = -1
        self.food = -1
        self.foodLeft = -1
        self.foodTop = -1
        self.foodRight = -1


def hasCollided(building,bird):
    if ((building.top+7 < bird.bottom) and (building.left+10 < bird.right) and (building.right-15 > bird.left)):
        return 1
    else:
        return 0

def hasCollectFood(food,bird,health):
    if(food.food == -1):
        return
    a = b = c = 0
    if (food.foodTop < bird.bottom):
        if((food.foodLeft < bird.right) and (food.foodRight > bird.right)):
            #print("Food!")
            a = 1
        if((food.foodLeft < bird.left) and (food.foodRight > bird.left)):
            #print("Food!")
            b = 1
        if((food.foodLeft > bird.left) and (food.foodRight < bird.right)):
            #print("Food!")
            c = 1
        if(a or b or c):
            health[0] = 100
            food.food = -1


def drawObs(rect1,level):
    if(rect1.rand == -1):
        rect1.rand = random.randrange(150, 499)
        rect1.rand = (int(rect1.rand) / 100) * 100
        rect1.posHor = 900
        height = 600 - rect1.rand
        #pygame.draw.rect(Canvas, blue, (rect1.posHor , 0, 250, rect1.rand), 2)
        pygame.draw.rect(Canvas, build, (rect1.posHor , rect1.rand + 100, 300, 600-rect1.rand), 0)
        rect1.left = rect1.posHor
        rect1.top = rect1.rand + 100
        rect1.right = rect1.left + 300

        foodRand = random.randrange(0,50)
        if(foodRand % 2 == 0):
            rect1.food = 1
            rect1.foodLeft = rect1.posHor + random.randrange(1,270)
            rect1.foodRight = rect1.foodLeft + 30
            rect1.foodTop = rect1.rand + 100 - 50

        while(height>0):
            pygame.draw.rect(Canvas, glass, (rect1.posHor + 25 , 600 - height +25, 100, 50), 0)
            pygame.draw.rect(Canvas, glass, (rect1.posHor + 25 + 150 , 600 - height +25, 100, 50), 0)
            height = height - 100
    else:
        if(rect1.posHor - 10 > -300):
            rect1.posHor = rect1.posHor-5 - level
            #pygame.draw.rect(Canvas, blue, (rect1.posHor , 0, 250, rect1.rand), 2)
            pygame.draw.rect(Canvas, build, (rect1.posHor , rect1.rand + 100, 300, 600-rect1.rand), 0)
            height = 500 - rect1.rand
            rect1.left = rect1.posHor
            rect1.top = rect1.rand + 100
            rect1.right = rect1.left + 300

            if(rect1.food == 1):
                rect1.foodLeft = rect1.foodLeft - 5 - level
                rect1.foodRight = rect1.foodLeft + 30
                rect1.foodTop = rect1.rand + 100 - 50

            while(height>0):
                pygame.draw.rect(Canvas, glass, (rect1.posHor + 25 , 600 - height +25, 100, 50), 0)
                pygame.draw.rect(Canvas, glass, (rect1.posHor + 25 + 150 , 600 - height +25, 100, 50), 0)
                height = height - 100
        else:
            rect1.reset()


#intialising variables

window_height=600
window_width=900
a = b = 250
blue = (0, 0, 225)
glass = (0, 0, 51)
white = (255,255,255)
sky = (170, 223, 255)
build = (192, 192, 192)

fps = 30
font = pygame.font.SysFont(None, 28)
mainClock = pygame.time.Clock()

level = 0
health = 100

Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MINI PROJECT')

FOODimage = pygame.image.load('food.png')
FOODrect = FOODimage.get_rect()

BIRDimage = pygame.image.load('bird4.png')
BIRDrect = BIRDimage.get_rect()
BIRDrect.centerx = BIRDrect.centery = 250
speedX = 0
speedY = 0

a = random.randrange(150, 499)
a = (int(a) / 100) * 100
rect1 = rect(a,900)
a = random.randrange(150, 499)
a = (int(a) / 100) * 100
rect2 = rect(a,1300)
a = random.randrange(150, 499)
a = (int(a) / 100) * 100
rect3 = rect(a,1700)

frameMod = 0
dist = 0

gameOn = 0

while (not gameOn):
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if event.key == K_SPACE:
                gameOn = 1

    Msg = "DESI BIRD"
    msgPos = font.render(Msg, 1, blue)
    msgRec = msgPos.get_rect()
    msgRec.topleft = (10,10)

    Msg2 = "PRESS SPACE BAR TO START GAME"
    msgPos2 = font.render(Msg2, 1, blue)
    msgRec2 = msgPos2.get_rect()
    msgRec2.topleft = (10,30)

    Msg3 = "> Your health will start declining after flying 30 m"
    msgPos3 = font.render(Msg3, 1, blue)
    msgRec3 = msgPos3.get_rect()
    msgRec3.topleft = (10,60)

    Msg4 = "> Collect the food over the buildings to restore health"
    msgPos4 = font.render(Msg4, 1, blue)
    msgRec4 = msgPos4.get_rect()
    msgRec4.topleft = (10,80)

    Canvas.fill(white)
    Canvas.blit(msgPos,msgRec)
    Canvas.blit(msgPos2,msgRec2)
    Canvas.blit(msgPos3,msgRec3)
    Canvas.blit(msgPos4,msgRec4)
    pygame.display.update()

exitGame = 0

while(not exitGame):

    a = random.randrange(150, 499)
    a = (int(a) / 100) * 100
    rect1 = rect(a,900)
    a = random.randrange(150, 499)
    a = (int(a) / 100) * 100
    rect2 = rect(a,1300)
    a = random.randrange(150, 499)
    a = (int(a) / 100) * 100
    rect3 = rect(a,1700)

    BIRDrect.centerx = BIRDrect.centery = 250
    speedX = 0
    speedY = 0
    health = 100

    frameMod = 0
    dist = 0


    while gameOn:     # the main game loop

        if(dist/10 > 30):
            health = health-0.3
        dist += 1
        if(dist%500 == 0):
            level += 1
        frameMod = frameMod % 25
        if(frameMod % 5 == 0):
            BIRDimage = pygame.image.load('bird4.png')
            BIRDrect = BIRDimage.get_rect()
            BIRDrect.centerx = a
            BIRDrect.centery = b

        for event in pygame.event.get():
            if ((event.type == KEYDOWN) and health>0):

                if event.key == K_UP:
                    BIRDimage = pygame.image.load('bird2.png')
                    BIRDrect = BIRDimage.get_rect()
                    BIRDrect.centerx = a
                    BIRDrect.centery = b
                    Canvas.blit(BIRDimage, BIRDrect)
                    frameMod = 0
                    speedY = speedY - 7 - (level/6)
                if event.key == K_DOWN:
                    BIRDimage = pygame.image.load('bird3.png')
                    BIRDrect = BIRDimage.get_rect()
                    BIRDrect.centerx = a
                    BIRDrect.centery = b
                    Canvas.blit(BIRDimage, BIRDrect)
                    frameMod = 0
                    speedY = speedY + 2 + (level/8)
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


        if ((BIRDrect.top > 0) and (BIRDrect.bottom < 600)):
            BIRDrect.top += speedY
        else:
            speedY *= 0
            BIRDrect.top = 5

        if ((BIRDrect.left > 0) and (BIRDrect.right < 900)):
            BIRDrect.left += speedX
        else:
            speedX *= 0
            if(BIRDrect.right > 900):
                BIRDrect.right = 900-5
            elif(BIRDrect.left < 0):
                BIRDrect.left = 5

        speedY+=0.2

        #getting the position of the BIRD
        a = BIRDrect.centerx
        b = BIRDrect.centery
        x = str(BIRDrect.centerx)
        y = str(BIRDrect.centery)

        distStr = str(dist/10)
        distStr = "Distance: " + distStr + " m"
        pos_dist = font.render(distStr , 1, blue)
        healthStr = "Health: " + str(health) + "%"
        pos_health = font.render(healthStr, 1, blue)

        distRec = pos_dist.get_rect()
        HealthRec = pos_health.get_rect()


        distRec.topleft = (10,10)
        HealthRec.topleft = (180,10)

        if(hasCollided(rect1,BIRDrect)):
            gameOn = 0
        if(hasCollided(rect2,BIRDrect)):
            gameOn = 0
        if(hasCollided(rect3,BIRDrect)):
            gameOn = 0

        healthCont = [health]
        hasCollectFood(rect1,BIRDrect,healthCont)
        hasCollectFood(rect2,BIRDrect,healthCont)
        hasCollectFood(rect3,BIRDrect,healthCont)
        health = healthCont[0]

       # BackImage = pygame.image.load('back.jpg')
        # BackRect = BackImage.get_rect()
       # BackRect.topleft = (0,0)


        Canvas.fill(sky)
       # Canvas.blit(BackImage, BackRect)
        Canvas.blit(BIRDimage, BIRDrect)
        Canvas.blit(pos_dist,distRec)
        Canvas.blit(pos_health,HealthRec)
        drawObs(rect1,level)
        if(rect1.food == 1):
            FOODrect.centerx = rect1.foodLeft + 15
            FOODrect.centery = rect1.foodTop + 15
            Canvas.blit(FOODimage, FOODrect)
        drawObs(rect2,level)
        if(rect2.food == 1):
            FOODrect.centerx = rect2.foodLeft + 15
            FOODrect.centery = rect2.foodTop + 15
            Canvas.blit(FOODimage, FOODrect)
        drawObs(rect3,level)
        if(rect3.food == 1):
            FOODrect.centerx = rect3.foodLeft + 15
            FOODrect.centery = rect3.foodTop + 15
            Canvas.blit(FOODimage, FOODrect)
        pygame.display.update()

        mainClock.tick(fps)
        frameMod += 1

    exitMenu = 1
    HighScore = 0

    try:
        file = open('hiScore.txt', 'r')
        HighScore = file.read()
        HighScore = int(HighScore)
        HS = HighScore
    except:
        f = open('hiScore.txt','w')
        distStr = str(dist/10)
        f.write(distStr)
        f.close()
        HS = distStr

    if(dist/10 > HighScore):
        HS = dist/10
        f = open('hiScore.txt','w')
        distStr = str(dist/10)
        f.write(distStr)
        f.close()

    while((not exitGame) and exitMenu):
        Msg1 = "OOPS! you crashed into a building!"
        msgPos1 = font.render(Msg1, 1, blue)
        msgRec1 = msgPos1.get_rect()
        msgRec1.topleft = (10,10)

        Msg2 = "You flew " + str(dist/10) + " m"
        msgPos2 = font.render(Msg2, 1, blue)
        msgRec2 = msgPos2.get_rect()
        msgRec2.topleft = (10,30)

        Msg5 = "HIGH SCORE: " + str(HS)
        msgPos5 = font.render(Msg5, 1, blue)
        msgRec5 = msgPos5.get_rect()
        msgRec5.topleft = (10,110)
        Canvas.blit(msgPos5,msgRec5)

        Msg3 = "PRESS SPACE BAR TO FLY AGAIN"
        msgPos3 = font.render(Msg3, 1, blue)
        msgRec3 = msgPos3.get_rect()
        msgRec3.topleft = (10,60)

        Msg4 = "PRESS ESCAPE TO EXIT"
        msgPos4 = font.render(Msg4, 1, blue)
        msgRec4 = msgPos4.get_rect()
        msgRec4.topleft = (10,80)

        Canvas.fill(white)
        Canvas.blit(msgPos,msgRec)
        Canvas.blit(msgPos2,msgRec2)
        Canvas.blit(msgPos3,msgRec3)
        Canvas.blit(msgPos4,msgRec4)
        Canvas.blit(msgPos5,msgRec5)
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if event.key == K_SPACE:
                    gameOn = 1
                    exitMenu = 0
                if event.key == K_ESCAPE:
                    gameOn = 0
                    exitGame = 1
        pygame.display.update()

pygame.display.update()
