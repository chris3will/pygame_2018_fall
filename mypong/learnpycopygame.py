#2018/11/30
#综合楼B开始着手进行大作业

import pygame
import sys
import os
os.chdir(r'D:\\code\\tlpython\\pygame\\mypong')
pygame.init()

width,height=640,480
size = 640, 480
ball_width = 10
ball_height = 10
xpos = 0
ypos=60

screen = pygame.display.set_mode(size)
bgcolour=0x2F,0x4F,0x4F
print(os.getcwd())
bat = pygame.image.load("bat.png").convert()
batrect = bat.get_rect()
batrect=batrect.move(320,150)

#batrect=batrect.move((width-batrect.width)/2,height-batrect.height-10)
ball = pygame.image.load("ball.png").convert()
ballrect = ball.get_rect()

ball_width = ballrect.width
ball_height=ballrect.height

clock = pygame.time.Clock()
row = 0
ballnew_rect = []
adj=0

brick = pygame.image.load("brick.png").convert()
brickrect = brick.get_rect()
brickwidth = brickrect.width
brickheight = brickrect.height

xpos = 0
ypos = 60
adj = 0

all_brick_rect = []

for i in range(0, 52):
        new = brick.get_rect()
        new = new.move(xpos, ypos)
        all_brick_rect.append(new)
        xpos += brickwidth
        if xpos > width:
                if adj == 0:
                        adj = brickwidth / 2
                else:
                        adj = 0
                xpos = -adj
                ypos=ypos+brickheight
for i in all_brick_rect:
        print(i)

while (True):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
        #batrect = batrect.move(5, 0)
        #print(batrect[0])
        
        for i in range(0,len(brickrect)):
               
                screen.blit(brick,all_brick_rect[i])
        #screen.fill(bgcolour)
        #screen.blit(bat,batrect)
        pygame.display.flip()