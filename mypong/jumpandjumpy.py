import sys, pygame, random
import pygame.freetype,time


width, height = (500, 600)

black = (0,0,0)
white = (255, 255, 255)
green = (0,255,0)
brown = (210, 105, 30)
pink = (255, 192, 203)



class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\bluebird-downflap.png").convert()
        #self.image.fill((255, 192, 203))
        #self.image=pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\dinosaur.png")
        self.rect = self.image.get_rect()
        

        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.jumpflag=1
        self.grav = 4 # Gravity
        self.lift  = -32 # Force applied to rect when jumping
        self.vel = [0, 0] # x, y
    
    # Translate position into rectangle position
    def render(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def update(self):
        # Vertical movement
        self.vel[1] -= self.grav * 0.8
        self.pos[1] -= self.vel[1]
    
        self.pos[0]+=self.vel[0]

        self.vel[0] *=  0.90  # De accelerate horizontal movement

        # Limit horizontal acceleration
        if abs(self.vel[0]) > 15:
            if self.vel[0] < 0:
                self.vel[0] == -15
            elif self.vel[0] > 0:
                self.vel[0] == 15

        # Limit veritcal movement
        if abs(self.vel[1]) > 10:
            if self.vel[1] < 0:
                self.vel[1] == -10
                

        # Bounds
        if not player_has_jumped:
            if self.pos[1] > 450 - 20:
                    self.vel[1] = 0  
                    self.pos[1] = 450 - 20 
        
    
    # Basic movements controls
    def jump(self):
        #self.pos[1] -= 20
        self.vel[1] -= self.lift


    def move_left(self):
        if self.rect.left <= 0:
            self.vel[0]=500
        else:
            self.vel[0] = -10.5
    
    def move_right(self):
        if self.rect.right >= 500:
            self.vel[0] = -500-self.rect.width
        else:
            self.vel[0] = 10.5 

    def check_for_gameover(self):
        if self.rect.y  >= 600:
            return True

class Boards(pygame.sprite.Sprite):
    def __init__(self, pos_y):
        super().__init__()
        #self.length = random.randint(10, 150)
        #self.image = pygame.Surface((self.length, Boards.board_height))
        #self.image.fill(brown)
        i = random.randint(0, 1)
        self.spe=0
        if (i == 0):
            self.spe=0
            self.image = pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\gameover.png")
        else:
            self.spe=1
            self.image = pygame.image.load("D:\code\\tlpython\pygame\FlapPyBird-master\\assets\sprites\\dinosaur_down_left.png")
        
        
        self.rect = self.image.get_rect()
        self.hasdo=0
        self.y_gap = pos_y
        self.x = int(random.randint(0, width - self.rect.width))
        self.rect.x=self.x 
        self.y = pos_y

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y - self.y_gap - 20 # Minus 10 just generate out of picture

    def move(self):
        self.y += game_speed

def game():
    fly=1
    
    
    while(fly):
        screen = pygame.display.set_mode((width, height))

        pygame.freetype.init()
        game_font = pygame.freetype.SysFont("Arial", 24,1)
        all_sprites_list = pygame.sprite.Group()
        board_sprites_list = pygame.sprite.Group()
        Clock = pygame.time.Clock()
    
        ball = Ball([width/2, 450 - 20])
        
        
        all_sprites_list.add(ball)
    
        board_height_counter = 1
        global player_has_jumped
        global game_speed
        game_speed = 2.5
        game_score = 0

        player_has_jumped = False
        running=True
        # Game loop
        pause = 0
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pause >0:
                        pause-=1  
                    if event.key == pygame.K_p:
                        pause = 2
                        print(pause)
                        game_font.render_to(screen, (50, 200), "POSE POSE, Any to continue, except p", pink)
                        pygame.display.flip()
                    if event.key == pygame.K_s:
                        if game_speed > 1:
                            game_speed -= 1
                        else:
                            game_speed=1

                                    
                    if event.key == pygame.K_SPACE:
                        if  ball.jumpflag == 1:
                            ball.jump()
                            ball.jumpflag=0
                            player_has_jumped = True
                    
                    
                        
                       
            if (pause == 0):
                #print(pause)
                # Smooth movement left and right
                if pygame.key.get_pressed()[97] or pygame.key.get_pressed()[276]:
                    ball.move_left()
        
                elif pygame.key.get_pressed()[100] or pygame.key.get_pressed()[275]:
                    ball.move_right()
        
                if ball.pos[1] > 450:#危险警戒
                    screen.fill(black)
                else:
                    screen.fill(white) # Draw white background
        
                ball.update()#更新球的行为,这里从网上借鉴的觉得有些鸡肋
                ball.render()

                if ball.check_for_gameover():
                    game_speed = 0
                    board_sprites_list.empty()
                #game_font.render_to(screen, (200, 250), 'HALI LUYA!')
                    running=False


                if not player_has_jumped:
                    pygame.draw.line(screen, pink, (0, 450), (width, 450),2) # Base line

                # Generate random boards 
                if board_height_counter > 0:
                    y = random.randrange(75 ,140,26)
                    board_sprites_list.add(Boards(y))
                    board_height_counter -= y 

                board_sprites_list.draw(screen)
                board_sprites_list.update()

                # Collioson detection between player and boards
                for board in board_sprites_list:
                    board.move()
                    if pygame.sprite.collide_rect(ball, board):
                        if ball.rect.top>=(board.rect.top-board.rect.height/2):
                            if (board.hasdo == 0):
                                #这个板子还没有被踩过
                                game_score += 1+board.spe
                                board.hasdo = 1
                            if player_has_jumped:
                                    ball.pos[1] = board.rect.y - 15
                                    ball.vel[1] = 0
                        ball.jumpflag=1                        


                board_height_counter += game_speed
                #加速机制        
                if game_score > 7.5 * game_speed:
                    game_speed += 1
                if  running:
                    game_font.render_to(screen, (400, 500), 'Score: ' + str(game_score),(0x33, 0xFF, 0x33))
                
                #刷新对象
                all_sprites_list.draw(screen)
                pygame.display.flip()

                Clock.tick(30)
        
        
        game_font.render_to(screen, (125, 200), 'Your finall Score: ' + str(game_score), brown)
        game_font.render_to(screen, (195, 260), 'Enter Y to rejoin us !!' , pink)
        
        pygame.display.flip()
        shit=1
        while(shit):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:  
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_y:
                            fly = 1
                            shit=0
                        else:
                            fly = 0
                            print(pygame.K_LEFT)
                            print(pygame.K_RIGHT)
    #time.sleep(5)

def surface():
    screen = pygame.init()
    game()
    
if __name__ == '__main__':
    
    running = 1
    while (running):

        surface()
    