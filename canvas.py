import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200, 110))
color = (255, 0, 0)
pygame.display.set_caption('Draw Rectangle')

while True: # main loop
    for event in pygame.event.get():
        pygame.draw.rect(screen, color, pygame.Rect(10, 10, 40, 40))

        pygame.draw.rect(screen, color, pygame.Rect(60, 10, 40, 40), 5)
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
