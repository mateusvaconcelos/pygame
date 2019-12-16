import pygame
pygame.init()

win = pygame.display.set_mode((700,500))

pygame.display.set_caption("...:APOCALYPSO:...")

walkRight = [pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R1.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R2.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R3.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R4.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R5.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R6.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R7.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R8.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R9.png')]
walkLeft = [pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L1.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L2.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L3.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L4.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L5.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L6.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L7.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L8.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L9.png')]
bg = pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/bd.jpg')
char = pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/standing.png')
run_it = Control()

clock = pygame.time.Clock()

# bulletSound = pygame.mixer.Sound('C:/Users/900149/Desktop/Pygame-Tutorials/Game/music/bullet.wav')
# hitSound = pygame.mixer.Sound('C:/Users/900149/Desktop/Pygame-Tutorials/Game/music/hit.wav')

# music = pygame.mixer.music.load('C:/Users/900149/Desktop/Pygame-Tutorials/Game/music/music.mp3')
# pygame.mixer.music.play(-1)

vidas = 3
 
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 0
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-1', 1, (0,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        if vidas == 0:
            pygame.quit()
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R1E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R2E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R3E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R4E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R5E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R6E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R7E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R8E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R9E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R10E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/R11E.png')]
    walkLeft = [pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L1E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L2E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L3E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L4E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L5E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L6E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L7E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L8E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L9E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L10E.png'), pygame.image.load('C:/Users/vasconcelos/Desktop/pygame/Game maykon/image/L11E.png')]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class Control(object):
    """Classe para gerenciar loop de eventos e estados de jogos."""
    def __init__(self):
        """Inicialize a tela e prepare os objetos do jogo."""
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.keys = pg.key.get_pressed()
        self.done = False
        self.player = Player((50,875), 4)
        self.level = pg.Surface((1000,1000)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = self.screen.get_rect(bottom=self.level_rect.bottom)
        self.win_text,self.win_rect = self.make_text()
        self.obstacles = self.make_obstacles()

    def make_text(self):
        """Renderiza um objeto de texto. O texto é renderizado apenas uma vez."""
        font = pg.font.Font(None, 50)
        message = "Vagabundo vai estuda para de joga"
        text = font.render(message, True, (100,100,175))
        rect = text.get_rect(centerx=self.level_rect.centerx, y=100)
        return text, rect

    def make_obstacles(self):
        """Adiciona alguns obstáculos arbitrariamente colocados a um sprite.."""
        walls = [Block(pg.Color("magenta"), (0,980,1000,20)),
                 Block(pg.Color("magenta"), (0,0,20,1000)),
                 Block(pg.Color("magenta"), (980,0,20,1000))]
        static = [Block(pg.Color("violet"), (250,780,200,100)),
                  Block(pg.Color("violet"), (600,880,200,100)),
                  Block(pg.Color("violet"), (20,360,880,40)),
                  Block(pg.Color("violet"), (950,400,30,20)),
                  Block(pg.Color("violet"), (20,630,50,20)),
                  Block(pg.Color("violet"), (80,530,50,20)),
                  Block(pg.Color("violet"), (130,470,200,215)),
                  Block(pg.Color("violet"), (20,760,30,20)),
                  Block(pg.Color("violet"), (400,740,30,40))]
        moving = [MovingBlock(pg.Color("yellow"), (20,740,75,20), 300, 0),
                  MovingBlock(pg.Color("yellow"), (600,500,100,20), 700, 0),
                  MovingBlock(pg.Color("yellow"),
                              (420,430,100,20), 550, 1, speed=3, delay=200),
                  MovingBlock(pg.Color("yellow"),
                              (450,700,50,20), 930, 1, start=930),
                  MovingBlock(pg.Color("yellow"),
                              (500,700,50,20), 730, 0, start=730),
                  MovingBlock(pg.Color("yellow"),
                              (780,700,50,20), 895, 0, speed=-1)]
        return pg.sprite.Group(walls, static, moving)
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('vidas : ' + str(vidas), 1, (0,0,0))
    win.blit(text, (350, 10))
    maykon.draw(win)
    Chimbinha.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
maykon = player(300, 410, 64,64)
Chimbinha = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if Chimbinha.visible == True:
        if maykon.hitbox[1] < Chimbinha.hitbox[1] + Chimbinha.hitbox[3] and maykon.hitbox[1] + maykon.hitbox[3] > Chimbinha.hitbox[1]:
            if maykon.hitbox[0] + maykon.hitbox[2] > Chimbinha.hitbox[0] and maykon.hitbox[0] < Chimbinha.hitbox[0] + Chimbinha.hitbox[2]:
                maykon.hit()
                vidas -= 1

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < Chimbinha.hitbox[1] + Chimbinha.hitbox[3] and bullet.y + bullet.radius > Chimbinha.hitbox[1]:
            if bullet.x + bullet.radius > Chimbinha.hitbox[0] and bullet.x - bullet.radius < Chimbinha.hitbox[0] + Chimbinha.hitbox[2]:
                #hitSound.play()
                Chimbinha.hit()
                #vidas += 1
                bullets.pop(bullets.index(bullet))
                
                
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        #bulletSound.play()
        if maykon.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(maykon.x + maykon.width //2), round(maykon.y + maykon.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and maykon.x > maykon.vel:
        maykon.x -= maykon.vel
        maykon.left = True
        maykon.right = False
        maykon.standing = False
    elif keys[pygame.K_RIGHT] and maykon.x < 500 - maykon.width - maykon.vel:
        maykon.x += maykon.vel
        maykon.right = True
        maykon.left = False
        maykon.standing = False
    else:
        maykon.standing = True
        maykon.walkCount = 0
        
    if not(maykon.isJump):
        if keys[pygame.K_UP]:
            maykon.isJump = True
            maykon.right = False
            maykon.left = False
            maykon.walkCount = 0
    else:
        if maykon.jumpCount >= -10:
            neg = 1
            if maykon.jumpCount < 0:
                neg = -1
            maykon.y -= (maykon.jumpCount ** 2) * 0.5 * neg
            maykon.jumpCount -= 1
        else:
            maykon.isJump = False
            maykon.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()


