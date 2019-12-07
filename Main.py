import pygame

# Initialize pygame
pygame.init()

# Create the screen 800x600
screen = pygame.display.set_mode((800, 600))

#Caption and Icon
pygame.display.set_caption("Carrom Legends")
icon=pygame.image.load("black dragon.png")
pygame.display.set_icon(icon)

#Striker
strikerimg=pygame.image.load('strikersmall.png')
strikerx = 370
strikery = 480

def striker():
    screen.blit(strikerimg,(strikerx,strikery))

# Game Loop
running = True
while running:
    #screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    striker()
    pygame.display.update()