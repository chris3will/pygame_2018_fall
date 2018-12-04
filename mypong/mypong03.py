import pygame,sys

width = 640
height = 480
size = width, height
pygame.init()
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
