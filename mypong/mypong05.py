import pygame,sys

width = 640
height = 480
size = width, height
pygame.init()
screen = pygame.display.set_mode(size)
bgcolour = 0x2F, 0x4F, 0x4F

bat = pygame.image.load("bat.png").convert()
batrect = bat.get_rect()
batrect = batrect.move((width-batrect.width)/2,height-batrect.height-10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bgcolour)

    screen.blit(bat, batrect)

    pygame.display.flip()
