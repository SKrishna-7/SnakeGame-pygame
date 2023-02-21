#@sureshkrishna
import pygame
import sys
import time
import random

pygame.init()
pygame.mixer.init(frequency= 44100,size=-16,channels=2,buffer=512)
clock=pygame.time.Clock()

#------------------GameVariables-----------------------------
ScreenX=500
ScreenY=500
x,y=100,200
width,height=20,20
speed=5
DirX=0
DirY=0
FoodX,FoodY=0,0
SnakeLength=1
SnakeList=[]
FScore=0
GameOverSrc=pygame.image.load('assests/gameover.png')
GOrect=GameOverSrc.get_rect(center=(ScreenX/2,ScreenY/2-50))
GAMEOVER=False
#------ColorVariables-------
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
#------------------------------------------------------------
#-----------------Game Functions-----------------------------
def Food():
    FoodX=random.randint(0,ScreenX)
    FoodY=random.randint(0,ScreenY)
    return FoodX,FoodY

#-----------------------------------------
flap=pygame.mixer.Sound('assests/sfx_wing.wav')
hit=pygame.mixer.Sound('assests/sfx_hit.wav')
points=pygame.mixer.Sound('assests/sfx_point.wav')
die=pygame.mixer.Sound('assests/sfx_die.wav')
pygame.mixer.music.load('assests/pubg.mp3')
pygame.mixer.music.play(-1)

Screen=pygame.display.set_mode((ScreenX,ScreenX))
pygame.display.set_caption('SnakeGame')
font=pygame.font.SysFont(None,20)
Screen.fill(WHITE)

FoodX,FoodY=Food()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and GAMEOVER==False:
                flap.play()
                DirY=0
                DirY-=speed
                DirX=0
            if event.key==pygame.K_DOWN and GAMEOVER==False:
                flap.play()
                DirY=0
                DirY+=speed
                DirX=0
            if event.key==pygame.K_RIGHT and GAMEOVER==False:
                flap.play()
                DirX=0
                DirX+=speed
                DirY=0
            if event.key==pygame.K_LEFT and GAMEOVER==False:
                flap.play()
                DirX=0
                DirX-=speed
                DirY=0
            if event.key==pygame.K_SPACE and GAMEOVER==True:
                GAMEOVER=False
    x+=DirX
    y+=DirY
    if x>ScreenX:
        x=0
    elif x<0:
        x=ScreenX
    elif y>ScreenY:
        y=0
    elif y<0:
        y=ScreenY
    #-----------------
    
    Screen.fill(WHITE)
    if GAMEOVER==False:
        for x1,y1 in SnakeList:
           SnakeBox=pygame.draw.rect(Screen,(255,0,0),(x1,y1,width,height))
           FoodBox=pygame.draw.circle(Screen,GREEN,(FoodX,FoodY),8)

           if SnakeBox.colliderect(FoodBox):
                points.play()
                FoodX,FoodY=Food()
                SnakeLength+=10  
        SnakeList.append([x,y])
        if len(SnakeList)>SnakeLength:
           SnakeList.pop(0)
        if SnakeList[-1] in SnakeList[:-1]:
            GAMEOVER=True
            die.play()
            FScore=SnakeLength
            SnakeList.clear()
            SnakeLength=1
        Score=font.render(f"Score-{SnakeLength-1}",True,BLACK)
        Screen.blit(Score,(20,10))
    else:
        FinalScore=font.render(f'Score : {FScore-1}',True,BLACK)
        FSrect=FinalScore.get_rect(center=(ScreenX/2,250))
        ResumeText=font.render('Press Space to Start...',True,BLACK)
        RTrect=ResumeText.get_rect(center=(ScreenX/2,400))
        DevBy=font.render('Devloped By Sureshkrishna',True,RED)
        DevByrect=DevBy.get_rect(center=(ScreenX/2,480))

        Screen.blit(GameOverSrc,GOrect)
        Screen.blit(FinalScore,FSrect)
        Screen.blit(ResumeText,RTrect)
        Screen.blit(DevBy,DevByrect)

    clock.tick(120)    
    pygame.display.update()




#@sureshkrishna