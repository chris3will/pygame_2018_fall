import pygame,sys

bat_speed = 30
xspeed_init_value = 6
yspeed_init_value = 6

width = 640
height = 480
size = width, height
pygame.init()
screen = pygame.display.set_mode(size)
bgcolour = 0x2F, 0x4F, 0x4F

bat = pygame.image.load("bat.png").convert()
batrect = bat.get_rect()
batrect = batrect.move((width-batrect.width)/2,height-batrect.height-10)

ball = pygame.image.load("ball.png").convert()
ballrect = ball.get_rect()
ballrect = ballrect.move(width/2,height/3)

xspeed = xspeed_init_value
yspeed = yspeed_init_value

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 30)
pygame.mouse.set_visible(0)


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT:
                batrect = batrect.move(-bat_speed, 0)
                if batrect.left < 0:
                    batrect.left = 0
            if event.key == pygame.K_RIGHT:
                batrect = batrect.move(bat_speed, 0)
                if batrect.right > width:
                    batrect.right = width


    # move ball
    ballrect = ballrect.move(xspeed, yspeed)
    if ballrect.left < 0 or ballrect.right > width:
        xspeed = - xspeed
    if ballrect.top < 0:
        yspeed = - yspeed
    if ballrect.top > height:
        yspeed = - yspeed

    screen.fill(bgcolour)

    screen.blit(bat, batrect)
    screen.blit(ball, ballrect)

    pygame.display.flip()
