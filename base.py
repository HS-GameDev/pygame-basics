import pygame, sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock() #for fps

pygame.display.set_caption("my game")
WINDOW_SIZE = (800, 520)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300, 200))


while True:  #game loop
    display.fill((0,100,0)) #background color (red, green, blue)

    for event in pygame.event.get(): #loop for quit or any order
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    surf = pygame.transform.scale(display, WINDOW_SIZE) #create game window
    screen.blit(surf, (0,0)) #design window
    pygame.display.update() #update continous
    clock.tick(60) #60 fps
