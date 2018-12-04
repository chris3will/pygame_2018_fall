import pygame, sys

def maingame():
        xspeed_init_value = 6
        yspeed_init_value = 6
        
        pygame.init()

        bird = pygame.image.load("D:\code\\tlpython\\pygame\\flybird\bird0.png")
        
        bird_rect = bird.get_rect()
        birdwidth = bird_rect.width
        birdheight=bird_rect.height
        
        width = 640
        height = 480
        size = width, height
        xpos = 0
        ypos = 6
        
        screen=pygame.display.set_mode(size)

        all_bird = []
        for i in range(0, 48):
                newbird = bird.get_rect()
                newbird = newbird.move(xpos, ypos)
                all_bird.append(newbird)
                xpos = xpos + birdwidth
                
        while (True):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        sys.exit()
                
                for i in len(all_bird):
                        screen.blit(bird, all_bird[i])
                        
                pygame.display.flip()
                
maingame()

        