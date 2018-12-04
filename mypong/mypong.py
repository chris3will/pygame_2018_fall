import pygame,sys

def mainloop():
    xspeed_init_value = 6
    yspeed_init_value = 6
    bat_speed = 30
    width = 640
    height = 480
    size = width, height
    pygame.init()
    screen = pygame.display.set_mode(size)
    bgcolour = 0x2F, 0x4F, 0x4F

    bat = pygame.image.load("bat.png").convert()
    batrect = bat.get_rect()

    ball = pygame.image.load("ball.png").convert()
    ballrect = ball.get_rect()

    brick = pygame.image.load("brick.png").convert()
    bickrect = brick.get_rect()

    brick_width = bickrect.width
    brick_height = bickrect.height

    xpos = 0
    ypos = 60
    adj = 0

    all_brick_rect = []

    for i in range(0,52):
        new_rec = brick.get_rect()
        new_rec = new_rec.move(xpos ,ypos)
        all_brick_rect.append(new_rec)
        xpos = xpos + brick_width
        if xpos > width:
            if adj == 0:
                adj = brick_width/2
            else:
                adj = 0
            xpos = -adj
            ypos = ypos + brick_height

    batrect = batrect.move((width-batrect.width)/2,height-batrect.height-10)
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
                    batrect = batrect.move(-bat_speed,0)
                    if batrect.left < 0:
                        batrect.left = 0
                if event.key == pygame.K_RIGHT:
                    batrect = batrect.move(bat_speed,0)
                    if batrect.right > width:
                        batrect.right = width




        # check if ball hit then bat
        if ballrect.colliderect(batrect):
            yspeed = - yspeed

        #check if ball hit the wall
        for i in range(0, len(all_brick_rect)):
            if ballrect.colliderect(all_brick_rect[i]):
                all_brick_rect[i:i+1]=[]
                yspeed = - yspeed
                break

        # move ball
        ballrect = ballrect.move(xspeed, yspeed)
        if ballrect.left < 0 or ballrect.right > width:
            xspeed = - xspeed
        if ballrect.top < 0:
            yspeed = - yspeed
        if ballrect.top > height:
            yspeed = - yspeed

        screen.fill(bgcolour)
        
        for i in range(0, len(all_brick_rect)):
            screen.blit(brick, all_brick_rect[i])
        
        screen.blit(bat, batrect)
        screen.blit(ball, ballrect)
        #screen.blit(brick, bickrect)

        pygame.display.flip()


mainloop()