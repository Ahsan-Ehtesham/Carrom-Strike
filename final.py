##import pygame
##
##pygame.init()
##
##Display = pygame.display.set_mode((900, 630))
##
####set title
##
##pygame.display.set_caption("Carrom Club")
##player = pygame.image.load("coins2.png")
##striker1 = 370
##striker2 = 480
##striker1_change = 0
##
##
##def gamer(x, y):
##    Display.blit(player, (x, y))
##
##
##
##running = True
##while running:
##    Display.fill((0, 0, 0))
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##    gamer(striker1, striker2)
##    pygame.display.update()        

##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_RIGHT:
##                striker1_change = 0.1
##
##            if event.key == pygame.K_LEFT:
##                striker1_change = -0.1
##
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
##                striker1_change = 0
##
##    striker1 += striker1_change
##    gamer(striker1, striker2)
##      pygame.display.update()


import pygame
import random
import math


pygame.init()

screen = pygame.display.set_mode((700, 600))

##set title

pygame.display.set_caption("Carrom Club")

##striker = pygame.image.load("striker.png")
Board=pygame.image.load("Carromboard.jpg")
board1 = 50
board2 = 3
striker1_change = 0
def board(x, y):
    screen.blit(Board, (x, y))
black=pygame.image.load("black.png")


striker1 = 300
striker2 = 280
striker1_change = 0
def black1(x, y):
    screen.blit(black, (x, y))


striker3 = 260
striker4 = 280
def black2(x1, y1):
    screen.blit(black, (x1, y1))


striker5 = 340
striker6 = 280
def black3(x2, y2):
    screen.blit(black, (x2, y2))
    
striker7 = 220
striker8 = 280
def black4(x3, y3):
    screen.blit(black, (x3, y3))
striker9 = 280
striker10 = 300
def black5(x4, y4):
    screen.blit(black, (x4, y4))

striker11 = 280
striker12 = 260
def black6(x5, y5):
    screen.blit(black, (x5, y5))

    
## white coins
white=pygame.image.load('white.png')
striker13 = 320
striker14 = 280
def white1(x6, y6):
    screen.blit(white, (x6, y6))
    
striker15 = 240
striker16 = 280
def white2(x7, y7):
    screen.blit(white, (x7, y7))
    
striker17 = 280
striker18 = 280
def white3(x8, y8):
    screen.blit(white, (x8, y8))    

striker19 = 280
striker20 = 320
def white4(x9, y9):
    screen.blit(white, (x9, y9))
    
striker21 = 260
striker22 = 300
def white5(x10, y10):
    screen.blit(white, (x10, y10))

    
striker23= 280
striker24 = 240
def white6(x11, y11):
    screen.blit(white, (x11, y11))


##red coin


red=pygame.image.load("queen.png")
striker25= 300
striker26 = 300
def red1(x12, y12):
    screen.blit(red, (x12, y12))

    
running = True
while running:
    screen.fill((150,75,0))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board(board1,board2)       
    black1(striker1, striker2)
    black2(striker3,striker4)
    black3(striker5,striker6)
    black4(striker7,striker8)
    black5(striker9,striker10)
    black6(striker11,striker12)
    white1(striker13,striker14)
    white2(striker15,striker16)
    white3(striker17,striker18)
    white4(striker19,striker20)
    white5(striker21,striker22)
    white6(striker23,striker24)
    red1(striker25,striker26)
    pygame.display.update()
  





background_colour = (238,197,145)
(width, height) = (560,560)
drag = 0.999
elasticity = 0.75
gravity = (math.pi, 0.002)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
ORANGE=(255,165,0)
WOODEN =(238,197,145)


def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def collide(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors((p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass), (angle, 2*p2.speed*p2.mass/total_mass))
        (p2.angle, p2.speed) = addVectors((p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass), (angle+math.pi, 2*p1.speed*p1.mass/total_mass))
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5*(p1.size + p2.size - dist+1)
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap

class Particle():
    def __init__(self,colour, x, y, size,mass):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.mass=mass

        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag


    def strikers(self,ycor):
        (mX,mY) = pygame.mouse.get_pos()
        if mX>440:
           self.x=440
        elif mX<120:
           self.x=120
        else:
           self.x= mX
        self.y= ycor


    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

##screen = pygame.display.set_mode((800,560))
##pygame.display.set_caption('My Carrom ')
##
###number_of_particles = 10
##my_particles = []
##
###for n in range(number_of_particles):
###    size = random.randint(10, 20)
###    x = random.randint(size, width-size)
###    y = random.randint(size, height-size)
##
##striker = Particle(GREEN,160,470, 15,50)
##
##particle = Particle(BLACK,300,280, 10,5)
##my_particles.append(particle)
##particle = Particle(BLACK,260,280, 10,5)
##my_particles.append(particle)
##particle = Particle(BLACK,340,280, 10,5)
##my_particles.append(particle)
##particle = Particle(BLACK,220,280, 10,5)
##my_particles.append(particle)
##particle = Particle(BLACK,280,300, 10,5)
##my_particles.append(particle)
##particle = Particle(BLACK,280,260, 10,5)
##my_particles.append(particle)
##particle = Particle(ORANGE,280,280, 10,5)
##my_particles.append(particle)
##particle = Particle(WHITE,320,280, 10,5)
##my_particles.append(particle)
##particle = Particle(WHITE,240,280, 10,5)
##my_particles.append(particle)
##particle = Particle(WHITE,280,320, 10,5)
##my_particles.append(particle)
##particle = Particle(WHITE,260,300, 10,5)
##my_particles.append(particle)
##particle = Particle(WHITE,280,240, 10,5)
##my_particles.append(particle)
##
##particle = Particle(WHITE,100,320, 10,5)
##my_particles.append(particle)
##
##
##
##
##
##
##
##
##    #pygame.draw.line(screen,BLUE,(my_particles[0].x,my_particles[0].y),(mX,mY),2)
##
##
##

def back_color():
    screen.fill(background_colour)







selected_particle = None
running = True
state =0
count1=0
count2=0
flip=0
while running:

    screen.fill(background_colour)

##    """ Draw all circles"""
##    pygame.draw.circle(screen,BLACK,(280,280),60,1)
##    pygame.draw.circle(screen,BLACK,(20,20),20,0)
##    pygame.draw.circle(screen,BLACK,(540,20),20,0)
##    pygame.draw.circle(screen,BLACK,(20,540),20,0)
##    pygame.draw.circle(screen,BLACK,(540,540),20,0)
##
##    """ Draw all lines"""
##    pygame.draw.line(screen, BLACK, (120,80), (440,80), 3)
##    pygame.draw.line(screen, BLACK, (120,100), (440,100), 2)
##
##    pygame.draw.line(screen, BLACK, (80,120), (80,440), 3)
##    pygame.draw.line(screen, BLACK, (100,120), (100,440), 2)
##
##    pygame.draw.line(screen, BLACK, (120,460), (440,460), 2)
##    pygame.draw.line(screen, BLACK, (120,480), (440,480), 3)
##
##    pygame.draw.line(screen, BLACK, (460,120), (460,440), 2)
##    pygame.draw.line(screen, BLACK, (480,120), (480,440), 3)
##
##    """ Draw small circles"""
##
##    pygame.draw.circle(screen,RED,(120,90),10,0)
##    pygame.draw.circle(screen,RED,(440,90),10,0)
##
##    pygame.draw.circle(screen,RED,(90,120),10,0)
##    pygame.draw.circle(screen,RED,(90,440),10,0)
##
##    pygame.draw.circle(screen,RED,(120,470),10,0)
##    pygame.draw.circle(screen,RED,(440,470),10,0)
##
##    pygame.draw.circle(screen,RED,(470,120),10,0)
##    pygame.draw.circle(screen,RED,(470,440),10,0)
##
##    """ Draw inclined lines"""
##    pygame.draw.line(screen, BLACK, (60,500), (200,360), 1)
##    pygame.draw.line(screen, BLACK, (360,360), (500,500), 1)
##    pygame.draw.line(screen, BLACK, (60,60), (200,200), 1)
##    pygame.draw.line(screen, BLACK, (360,200), (500,60), 1)
##
##    """ Draw arrow lines"""
##    pygame.draw.line(screen, BLACK, (200,360), (200,400), 1)
##    pygame.draw.line(screen, BLACK, (200,360), (160,360), 1)
##
##    pygame.draw.line(screen, BLACK, (360,360), (360,400), 1)
##    pygame.draw.line(screen, BLACK, (360,360), (400,360), 1)
##
##    pygame.draw.line(screen, BLACK, (200,200), (160,200), 1)
##    pygame.draw.line(screen, BLACK, (200,200), (200,160), 1)
##
##    pygame.draw.line(screen, BLACK, (360,200), (400,200), 1)
##    pygame.draw.line(screen, BLACK, (360,200), (360,160), 1)
##
##    pygame.draw.line(screen, BLACK, (560,0), (560,560), 5)
##    pygame.draw.line(screen, BLACK, (0,0), (560,0), 10)
##    pygame.draw.line(screen, BLACK, (0,0), (0,560), 10)
##    pygame.draw.line(screen, BLACK, (0,560), (560,560), 10)
##
##
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if state == 0:
           if flip%2==0:
              ycor=470
           elif flip%2!=0:
              ycor=90

           striker.strikers(ycor)
           if event.type == pygame.MOUSEBUTTONDOWN:
               (mouseX, mouseY) = pygame.mouse.get_pos()
               if mouseX>440:
                   striker.x=440
               elif mouseX<120:
                   striker.x=120

               else:
                   striker.x=mouseX

               state =1
               continue

        if state ==1:
            if event.type == pygame.MOUSEBUTTONDOWN:
               (mouseX2, mouseY2) = pygame.mouse.get_pos()
               dx = mouseX2 - striker.x
               dy = mouseY2 - striker.y
               striker.angle = 0.5*math.pi + math.atan2(dy, dx)
               striker.speed = math.hypot(dx, dy) * .02
               state=2









    striker.move()
    striker.bounce()
    if striker.speed>0 and striker.speed<0.02:
        striker.x=160
        flip+=1
        if flip%2==0:
            striker.y=470
        elif flip%2!=0:
            striker.y=90
        if striker.x<30 and striker.speed>0:
            if striker.y<30:
                if flip%2==0:

                   count1-=1
                elif flip%2!=0:
                   count2-=1

        if striker.x<30 and striker.speed>0:
            if striker.y>530:
                if flip%2==0:

                   count1-=1
                elif flip%2!=0:
                   count2-=1

        if striker.x>530 and striker.speed>0:
            if striker.y<30:
                if flip%2==0:

                   count1-=1
                elif flip%2!=0:
                   count2-=1

        if striker.x>530 and striker.speed>0:
            if striker.y>530:
                if flip%2==0:

                   count1-=1
                elif flip%2!=0:
                   count2-=1

        striker.speed=0



        state=0


    for i, particle in enumerate(my_particles):

        particle.move()
        particle.bounce()
        collide(striker,particle)
        if particle.x<30 and particle.speed>0:
            if particle.y<30:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        if particle.x<30 and particle.speed>0:
            if particle.y>530:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        if particle.x>530 and particle.speed>0:
            if particle.y<30:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        if particle.x>530 and particle.speed>0:
            if particle.y>530:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1


        if count1!=0:
            print("1:"+ str(count1))
        if count2!=0:
            print ("2:" + str(count2))
        for particle2 in my_particles[i+1:]:

            collide(particle,particle2)

            striker.display()
            particle.display()
            if particle.speed<0.08:
                particle.speed=0




    pygame.display.flip()

















            #pygame.time.wait()'''

##
##
##
##
##
##
##
