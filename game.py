import pygame

#pygame setup
pygame.init()

#set resolution of our game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#load fishy
puffer_fish = pygame.image.load('puffer_fish.png')

#make background
background = pygame.Surface((WIDTH, HEIGHT))

#fill sky
background.fill((25,110,255)) #fill it with blue
#make a sandy rectangle
sand_height = 100
pygame.draw.rect(background, (255,200,105), (0, HEIGHT-sand_height, WIDTH, sand_height))

#draw the background
screen.blit(background, (0,0))

running = True
while running:
    #poll for events
    #pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #render your game here

    #flip(_) the display to put your work on the screen
    pygame.display.flip()