#########################################
# Programmer: Eitan Yehuda
# Date: 21/09/2012
# File Name: snake_template.py
# Description: This program is a template for Snake Game.
#               It demonstrates how to move and lengthen the snake. 
#########################################

import random
import pygame
pygame.init()

from random import randint
from math import sqrt

WIDTH  = 800
HEIGHT = 600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("background.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background, (800,600))
intro = pygame.image.load("intro.jpg")
intro = intro.convert_alpha()
intro = pygame.transform.scale(intro, (800,600))
exit_ = pygame.image.load("exit_button.png")
music = pygame.mixer.music.load("music.wav")
#music.play()
pygame.mixer.music.play(-1, 0)          #Plays music and repeats it indefinately

WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)
YELLOW = ( 255, 255, 0)
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)
BLACK = (  0,  0,  0)
outline = 0

#---------------------------------------#
# snake's properties                    #
#---------------------------------------#
BODY_SIZE = 5
HSPEED = 10
VSPEED = 10

appleX = random.randint(50,WIDTH-50)
appleY = random.randint(50,HEIGHT-50)
appleX2 = random.randint(50,WIDTH-50)
appleY2 = random.randint(50,HEIGHT-50)
appleR = 10
appleR2 = 10
appleSize = 1
appleSize2 = 1

speedX = 0
speedY = -VSPEED
segx = [int(WIDTH/2.)]*3
segy = [HEIGHT, HEIGHT+VSPEED, HEIGHT+2*VSPEED]
counter = 0
timer = 10
delay = 30

message = "GAME OVER"
message2 = "Apples Eaten: "
message3 = "Timer: "

#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#    
def redraw_screen():
    screen.blit(background,(0,0))
    for i in range(len(segx)):
        if i == 0:
            pygame.draw.polygon(screen, BLUE, [(segx[0],segy[0]-(BODY_SIZE+2)), (segx[0]-(BODY_SIZE+2),segy[0]), (segx[0],segy[0]+(BODY_SIZE+2)), (segx[0]+(BODY_SIZE+2),segy[0])])
        else:
            pygame.draw.circle(screen, YELLOW, (segx[i], segy[i]), BODY_SIZE, outline)
        pygame.draw.rect(screen, BLUE, (segx[-1]-BODY_SIZE, segy[-1]-BODY_SIZE, BODY_SIZE*2, BODY_SIZE*2))
    pygame.draw.circle(screen, RED, (appleX, appleY), appleR, outline)
    pygame.draw.circle(screen, GREEN, (appleX2, appleY2), appleR2, outline)
    text2 = font2.render(str(counter), 1, WHITE)
    text3 = font2.render(message2, 1, WHITE)
    text4 = font2.render(message3, 1, WHITE)
    text5 = font2.render(str(int(round(timer,0))), 1, WHITE)
    screen.blit(text2,(240,0))
    screen.blit(text3,(0,0))
    screen.blit(text4,(WIDTH-160,0))
    screen.blit(text5,(WIDTH-50,0))
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings

#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
inPlay = 1
print ("Use the arrows and the space br.")
while inPlay == 1:
    screen.blit(intro,(0,0))
    for event in pygame.event.get():    # check for any events
        
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER] or keys[pygame.K_ESCAPE] :
                inPlay = 2
        (cursorX,cursorY)=pygame.mouse.get_pos()       
        if event.type == pygame.MOUSEBUTTONDOWN:     
            if cursorX > 50 and cursorX < 318 and cursorY > 370 and cursorY < 479:
                inPlay = 2
                
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings
while inPlay == 2:
# check for events
    pygame.event.get()
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
            exit_flag = True                # Flag that we are done so we exit this loop

    keys = pygame.key.get_pressed()
# act upon key events
    if keys[pygame.K_LEFT] and speedX != HSPEED:
        speedX = -HSPEED
        speedY = 0
    elif keys[pygame.K_RIGHT] and speedX != -HSPEED:
        speedX = HSPEED
        speedY = 0
    elif keys[pygame.K_UP] and speedY != VSPEED:
        speedX = 0
        speedY = -VSPEED
    elif keys[pygame.K_DOWN] and speedY != -VSPEED:
        speedX = 0
        speedY = VSPEED
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    #if keys[pygame.K_SPACE]:            # if space bar is pressed, add a segment:
     #   segx.append(segx[-1])           # assign the same x and y coordinates
      #  segy.append(segy[-1])           # as those of the last segment
        
    font = pygame.font.SysFont("Ariel Black",150) #Define fonts
    font2 = pygame.font.SysFont("Ariel Black",50)
# move all segments
    for i in range(len(segx)-1,0,-1):   # start from the tail, and go backwards:
        segx[i]=segx[i-1]               # every segment takes the coordinates
        segy[i]=segy[i-1]               # of the previous one
# move the head
    segx[0] = segx[0] + speedX
    segy[0] = segy[0] + speedY
#eat apple
    if distance(segx[0], segy[0], appleX, appleY) <= appleR:
        if appleSize == 1:
            segx.append(segx[-1])           ## add 1 body segment
            segy.append(segy[-1])
        elif appleSize == 2:
            segx.append(segx[-1])           ## add 2 body segments
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
        elif appleSize == 3:
            segx.append(segx[-1])           ## add 3 body segments
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
        elif appleSize == 4:
            segx.append(segx[-1])           ## add 4 body segments
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
        elif appleSize == 5:
            segx.append(segx[-1])           ## add 5 body segments
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
            segx.append(segx[-1])           
            segy.append(segy[-1])
        timer=10                        #resets timer
        counter+=1
        appleX = random.randint(50,WIDTH-50)
        appleY = random.randint(50,HEIGHT-50)
        appleSize = random.randint(1,5)
        appleR = appleSize*10
        if counter%5 == 0:                #increase speed every 5 apples eaten
            delay-=4                     
        if timer > 9:                   #sets timer to 15 if apple eaten within 5 seconds
            timer = 15
    if distance(segx[0], segy[0], appleX2, appleY2) <= appleR2:
        if appleSize2 == 1:
            segx.remove(segx[-1])            ## remove 1 body segment
            segy.remove(segy[-1])
        elif appleSize2 == 2:
            segx.remove(segx[-1])           ## remove 2 body segments
            segy.remove(segy[-1])
            if len(segx) >= 2 :             ## if snake still alive(avoid error)
                segx.remove(segx[-1])           
                segy.remove(segy[-1])
        elif appleSize2 ==3:
            segx.remove(segx[-1])           ## remove 3 body segments
            segy.remove(segy[-1])
            if len(segx) >= 2 :             ## if snake still alive(avoid error)
                segx.remove(segx[-1])           
                segy.remove(segy[-1])
                if len(segx) >= 2 :             ## if snake still alive(avoid error)
                    segx.remove(segx[-1])       
                    segy.remove(segy[-1])
        elif appleSize2 ==4:
            segx.remove(segx[-1])           ## remove 4 body segments
            segy.remove(segy[-1])
            if len(segx) >= 2 :             ## if snake still alive(avoid error)
                segx.remove(segx[-1])           
                segy.remove(segy[-1])
                if len(segx) >= 2 :             ## if snake still alive(avoid error)
                    segx.remove(segx[-1])           
                    segy.remove(segy[-1])
                    if len(segx) >= 2 :             ## if snake still alive(avoid error)
                        segx.remove(segx[-1])
                        segy.remove(segy[-1])
        elif appleSize2 ==5:
            segx.remove(segx[-1])           ## remove 5 body segments
            segy.remove(segy[-1])
            if len(segx) >= 2 :             ## if snake still alive(avoid error)
                segx.remove(segx[-1])           
                segy.remove(segy[-1])
                if len(segx) >= 2 :             ## if snake still alive(avoid error)     
                    segx.remove(segx[-1])           
                    segy.remove(segy[-1])
                    if len(segx) >= 2 :             ## if snake still alive(avoid error)
                        segx.remove(segx[-1])           
                        segy.remove(segy[-1])
                        if len(segx) >= 2 :             ## if snake still alive(avoid error)            
                            segx.remove(segx[-1])           
                            segy.remove(segy[-1])
        timer=10                          #resets timer
        counter+=1
        appleX2 = random.randint(50,WIDTH-50)
        appleY2 = random.randint(50,HEIGHT-50)
        appleSize2 = random.randint(1,5)
        appleR2 = appleSize2*10
        if counter%5 == 0:                #increase speed every 5 apples eaten
            delay-=4
        if timer > 9:                   #sets timer to 15 if apple eaten within 5 seconds
            timer=15
        
            
#end        
    if segx[0] < 0 or segx[0] > WIDTH or segy[0] < 0 or segy[0] > HEIGHT:   #ends game if snake goes out play are(window borders)
        inPlay = 3
    if timer <= 0:                      #ends game if snake starves out(timer reaches 0)
        inPlay = 3
    if len(segx) < 2 :                  #ends game if only head is lef(body gone)
        inPlay = 3
    for i in range(len(segx)-1,0,-1):   #ends game if snake cuts itself
        if distance(segx[0], segy[0], segx[i],segy[i])<=BODY_SIZE:
            inPlay = 3
# update the screen     
    redraw_screen()
    pygame.time.delay(delay)
    timer-=0.001*delay                  #timer
while inPlay == 3:
    screen.fill(WHITE)
    screen.blit(exit_,(WIDTH/3-25,HEIGHT-200))
    text = font.render(message, 1, RED)
    text6 = font2.render(message2,1,BLACK)
    text7 = font2.render(str(counter),1,BLACK)
    screen.blit(text,(WIDTH/10,HEIGHT/4))
    screen.blit(text6,(WIDTH/3-5,HEIGHT/2-50))
    screen.blit(text7,(WIDTH/3+235,HEIGHT/2-50))
    pygame.display.update()

    
    for event in pygame.event.get():    # check for any events
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
                pygame.quit()                            # always quit pygame when done!
        (cursorX,cursorY)=pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:     
            if cursorX > 240 and cursorX < 532 and cursorY > 400 and cursorY < 550:
                pygame.quit()                            # always quit pygame when done!

