import pygame, sys, random, time
from pygame.locals import *

def maingame():
        xspeed_init_value = 6
        yspeed_init_value = 6
        
        pygame.init()
        clock=pygame.time.Clock()
        bird0 = pygame.image.load("D:\code\\tlpython\pygame\source\dinosaur_right.png")
        bird1 = pygame.image.load("D:\code\\tlpython\pygame\source\dinosaur_left.png")
        obstacle=pygame.image.load("D:\code\\tlpython\pygame\source\obstacle.png")
        
        bird=[bird0,bird1]
        background0=pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\background-day.png")
        background1=pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\background-night.png")
        base=pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\base.png")
        
        #加载计分牌
        score=[]*10
        score0=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\0.png')
        score1=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\1.png')
        score2=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\2.png')
        score3=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\3.png')
        score4=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\4.png')
        score5=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\5.png')
        score6=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\6.png')
        score7=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\7.png')
        score8=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\8.png')
        score9=pygame.image.load('D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\9.png')
        score.append(score0)
        score.append(score1)
        score.append(score2)
        score.append(score3)
        score.append(score4)
        score.append(score5)
        score.append(score6)
        score.append(score7)
        score.append(score8)
        score.append(score9)
        score_rects = []
        score_rect=score[0].get_rect()
        score_width = score_rect.width
        score_height = score_rect.height
        score_rects.append(score_rect.move(score_width, 0))
        score_rects.append(score_rect.move(2 * score_width, 0))
        score_rects.append(score_rect.move(3 * score_width, 0))

        goals=0
        

        loopIter=0


        basex = 0
        bgx=0
        baseShift=base.get_width()-background0.get_width()
        bgShift=background0.get_width()/8


        backgroundrect0 = background0.get_rect()
        
        bird_rect = bird[0].get_rect()
        bird_rect.top = 378
        bird_rect.left=0
        obstacle_init_rect = obstacle.get_rect()
        obstacle_init_rect.right = backgroundrect0.width
        obstacle_init_rect.top=372

        
        birdwidth = bird_rect.width
        birdheight = bird_rect.height
        

        #for action
        jumpflag = 1
        running=0
        jumping = 0
        falling=0
        jump_init_speed=-10
        
        width = 640
        height = 480
        
        


        all_bird_rect = []
        all_bird_rect.append(bird_rect)

        
        size = backgroundrect0.width,backgroundrect0.height
        background=[background0,background1]
        
        screen=pygame.display.set_mode(size)
        #pygame.key.set_repeat(1, 30)


        screen.blit(background[0],(0,0))
        while (True):
               
                jump_init_speed+=1
                if (loopIter + 1) % 5 == 0:
                    pass
                basex=-((-basex+4)%baseShift)
                #bgx=-((-bgx+5)%bgShift)
                #处理背景问题
                #backgroundrect=backgroundrect.move(i[flag],0)
                screen.blit(background[0], (bgx,0))
                #只设置跳跃按键，最多再添加一个导弹


            #对主龙进行处理    
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        sys.exit()
                                if event.key == pygame.K_UP or event.key==pygame.K_SPACE:
                                    #print(all_bird_rect)
                                    if jumpflag:
                                            jumping = 1
                                            jumpflag=0
                                    

                if(jumpflag==1):
                    if (jumping):
                        if(all_bird_rect[0].top >= (378 - 2 * birdheight)):
                            pygame.time.delay(10)
                            all_bird_rect[0] = all_bird_rect[0].move(0, -8)
                            screen.blit(bird0, all_bird_rect[0])
                        else:
                            jumping=0
                            falling=1
                print(jumpflag)

                if (all_bird_rect[0].top >= 378):
                    jumpflag = 1
                 
                if (falling == 1 and all_bird_rect[0].top < 378):
                    print(all_bird_rect[0])
                    all_bird_rect[0] = all_bird_rect[0].move(0, 6)
                flag = random.randint(0, len(bird) - 1)
                screen.blit(bird[flag], all_bird_rect[0])
                screen.blit(base, (basex, 420))

                #对记分牌进行处理
                for i in range(len(str(goals))):
                    if len(str(goals)) == 4:
                        sys.exit()
                    else:
                        screen.blit(score[int(str(goals)[-1])],score_rects[-1])
                        if len(str(goals))>=2:
                            screen.blit(score[int(str(goals)[-2])], score_rects[-2])
                        if len(str(goals))>=3:
                            screen.blit(score[int(str(goals)[-3])],score_rects[-3])
                    
                #对障碍物进行处理
                if(obstacle_init_rect):
                    screen.blit(obstacle,obstacle_init_rect)
                    obstacle_init_rect = obstacle_init_rect.move(-5, 0)
                    if obstacle_init_rect.left < all_bird_rect[0].left:
                        obstacle_init_rect=[]
                        goals += 1
                
                
                
                
                
                pygame.display.update()
                clock.tick(30)#frames per second setting
                pygame.display.flip()
                
                
maingame()

        