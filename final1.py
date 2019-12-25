import pygame
import random
import math

##Initialize pygame
pygame.init()
##Screensize
screen = pygame.display.set_mode((700, 600))

##set title
pygame.display.set_caption("Carrom Club")
##BgMusic
pygame.mixer.music.load('Desert_Skycut1.wav')
pygame.mixer.music.play(-1)

#Board
Board=pygame.image.load("Carromboard.jpg")
board1 = 50
board2 = 3
def board(x, y):
    screen.blit(Board, (x, y))

##Striker
strikerimg=pygame.image.load('striker.png')
strikerx = 285
strikery = 467
strikerx+=0.3

def striker(strikerx,strikery):
    screen.blit(strikerimg,(strikerx,strikery))

##black coins
black=pygame.image.load("black.png")
bc1 = 297
bc2 = 220
striker1_change = 0
def black1(x, y):
    screen.blit(black, (x, y))

bc3 = 348
bc4 = 292
def black2(x1, y1):
    screen.blit(black, (x1, y1))

bc5 = 260
bc6 = 300
def black3(x2, y2):
    screen.blit(black, (x2, y2))
    
bc7 = 214
bc8 = 280
def black4(x3, y3):
    screen.blit(black, (x3, y3))

bc9 = 339
bc10 = 190
def black5(x4, y4):
    screen.blit(black, (x4, y4))

bc11 = 350
bc12 = 342
def black6(x5, y5):
    screen.blit(black, (x5, y5))

## white coins
white=pygame.image.load('white.png')
wc1 = 345
wc2 = 240
def white1(x6, y6):
    screen.blit(white, (x6, y6))
    
wc3 = 305
wc4 = 320
def white2(x7, y7):
    screen.blit(white, (x7, y7))
    
wc5 = 255
wc6 = 250
def white3(x8, y8):
    screen.blit(white, (x8, y8))    

wc7 = 262
wc8 = 350
def white4(x9, y9):
    screen.blit(white, (x9, y9))
    
wc9 = 250
wc10 = 198
def white5(x10, y10):
    screen.blit(white, (x10, y10))

    
wc11= 390
wc12 = 260
def white6(x11, y11):
    screen.blit(white, (x11, y11))

##red coin

red=pygame.image.load("queen.png")
redx= 302
redy = 270
def red1(x12, y12):
    screen.blit(red, (x12, y12))

#Game Loop
running = True
while running:
    screen.fill((150,75,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type==pygame.MOUSEMOTION:
        (strikerx,strikery)=pygame.mouse.get_pos()
        if strikerx >= 465:
            strikerx=465
        elif strikerx <= 95:
            strikerx = 95
        strikery=465

    if event.type == pygame.MOUSEBUTTONDOWN:
        (strikerx, strikery) = pygame.mouse.get_pos()
        if strikerx > 440:
            striker.x = 440
        elif strikerx < 120:
            striker.x = 120
        else:
            striker.x = strikerx

    board(board1,board2)
    striker(strikerx, strikery)
    black1(bc1, bc2)
    black2(bc3,bc4)
    black3(bc5,bc6)
    black4(bc7,bc8)
    black5(bc9,bc10)
    black6(bc11,bc12)
    white1(wc1,wc2)
    white2(wc3,wc4)
    white3(wc5,wc6)
    white4(wc7,wc8)
    white5(wc9,wc10)
    white6(wc11,wc12)
    red1(redx,redy)
    pygame.display.update()