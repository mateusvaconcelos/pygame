'''Bolas de salto mudas

python .\logic\1car.py
'''

import pygame
import random
import sys


if sys.version_info[0]>2:
    xrange = range

SIZE = 640, 700
mv = pygame.image.load('logic/img/mv.png')
pygame.display.set_icon(mv)
pygame.display.set_caption("Carro")

def intn(*arg):
    '''Retornar lista de ints da tupla de arg'''
    return tuple(map(int,arg))

def Init(sz):
    '''Ative o PyGame'''
    global screen, screenrect
    pygame.init()
    screen = pygame.display.set_mode(sz)
    screenrect = screen.get_rect()

class GameMode:
    '''Modo de jogo básico'''
    def __init__(self):
        '''Definir modo de jogo
        - Inicializar fundo preto'''
        self.background = pygame.Color("black")
        

    def Events(self,event):
        '''Analisador de eventos'''
        pass

    def Draw(self, screen):
        '''Desenhar campo de jogo'''
        screen.fill(self.background)

    def Logic(self, screen):
        '''Lógica do jogo: o que calcular'''
        pass

    def Leave(self):
        '''O que fazer ao sair deste modo'''
        pass

    def Init(self):
        '''O que fazer ao entrar neste modo'''
        pass

class Ball:
    '''Classe de bola simples'''

    def __init__(self, filename, pos = (0.0, 0.0), speed = (0.0, 0.0)):
        '''Crie uma bola a partir da imagem'''
        self.fname = filename
        self.surface = pygame.image.load(filename)
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.pos = pos
        self.newpos = pos
        self.active = True

    def draw(self, surface):
        '''Desenhe uma bola na superfície'''
        surface.blit(self.surface, self.rect)

    def action(self):
        '''Prossiga com alguma ação'''
        if self.active:
            self.pos = self.pos[0]+self.speed[0], self.pos[1]+self.speed[1]

    def logic(self, surface):
        '''Interaja com a superfície do jogo
        - Verifique se a bola está fora de superfície, repouse-a e mude a aceleração ''
        '''
        x,y = self.pos
        dx, dy = self.speed
        if x < self.rect.width/2:
            x = self.rect.width/2
            dx = -dx
        elif x > surface.get_width() - self.rect.width/2:
            x = surface.get_width() - self.rect.width/2
            dx = -dx
        if y < self.rect.height/2:
            y = self.rect.height/2
            dy = -dy
        elif y > surface.get_height() - self.rect.height/2:
            y = surface.get_height() - self.rect.height/2
            dy = -dy
        self.pos = x,y
        self.speed = dx,dy
        self.rect.center = intn(*self.pos)

class Universe:
    '''Universo do jogo'''

    def __init__(self, msec, tickevent = pygame.USEREVENT):
        '''Executar um universo com msec tick'''
        self.msec = msec
        self.tickevent = tickevent

    def Start(self):
        '''Comece a correr'''
        pygame.time.set_timer(self.tickevent, self.msec)

    def Finish(self):
        '''Desligue um universo'''
        pygame.time.set_timer(self.tickevent, 0)

class GameWithObjects(GameMode):
    '''Modo de jogo com objetos ativos'''

    def __init__(self, objects=[]):
        '''Novo jogo com objetos ativos'''
        GameMode.__init__(self)
        self.objects = objects

    def locate(self, pos):
        '''Encontre objetos na posição pos'''
        return [obj for obj in self.objects if obj.rect.collidepoint(pos)]

    def Events(self, event):
        '''Analisador de eventos:

        - Execute a ação do objeto após cada tick'''
        GameMode.Events(self, event)
        if event.type == Game.tickevent:
            for obj in self.objects:
                obj.action()

    def Logic(self, surface):
        '''Lógica do jogo

        - Calcular o impacto dos objetos
        '''
        GameMode.Logic(self, surface)
        for obj in self.objects:
            obj.logic(surface)

    def Draw(self, surface):
        '''Desenhar campo de jogo

        - Desenhe todos os objetos no topo do campo de jogo
        '''
        GameMode.Draw(self, surface)
        for obj in self.objects:
            obj.draw(surface)

class GameWithDnD(GameWithObjects):
    '''Modo de jogo com objetos drad-n-droppeble'''
    def __init__(self, *argp, **argn):
        '''- Inicializar DnD'''
        GameWithObjects.__init__(self, *argp, **argn)
        self.oldpos = 0,0
        self.drag = None

    def Events(self, event):
        '''Analisador de eventos:

        - Suporte para arrastar e soltar objetos
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = self.locate(event.pos)
            if click:
                self.drag = click[0]
                self.drag.active = False
                self.oldpos = event.pos
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if self.drag:
                    self.drag.pos = event.pos
                    self.drag.speed = event.rel
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.drag:
                self.drag.active = True
                self.drag = None
        GameWithObjects.Events(self, event)

def __main__():
    '''Código do jogo principal'''
    global Game

    Init(SIZE)
    Game = Universe(50)

    Run = GameWithDnD()
    
    for teteu in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*5, 1+random.random()*5
        Run.objects.append(Ball("logic/img/1teteu.png",(x,y),(dx,dy)))
    for natan in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*5, 1+random.random()*5
        Run.objects.append(Ball("logic/img/natan.png",(x,y),(dx,dy)))
    
    for lista_rei in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*2, 1+random.random()*2
        Run.objects.append(Ball("logic/img/1teteu.png",(x,y),(dx,dy)))
    for gustavo in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*2, 1+random.random()*2
        Run.objects.append(Ball("logic/img/gustavo.png",(x,y),(dx,dy)))
    for vinicios in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*2, 1+random.random()*2
        Run.objects.append(Ball("logic/img/vini.png",(x,y),(dx,dy)))
    
    for maykon in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*2, 1+random.random()*2
        Run.objects.append(Ball("logic/img/lindo.png",(x,y),(dx,dy)))
    for abioluz in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*2, 1+random.random()*2
        Run.objects.append(Ball("logic/img/luz.png",(x,y),(dx,dy)))
    for bruno in xrange(0):
        x, y = random.randrange(screenrect.w), random.randrange(screenrect.h)
        dx, dy = 1+random.random()*2, 1+random.random()*2
        Run.objects.append(Ball("logic/img/bruno.png",(x,y),(dx,dy)))



    Game.Start()
    Run.Init()
    again = True
    while again:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            again = False
        Run.Events(event)
        Run.Logic(screen)
        Run.Draw(screen)
        pygame.display.flip()
    Game.Finish()
    pygame.quit()

if __name__ == '__main__':
    __main__()
