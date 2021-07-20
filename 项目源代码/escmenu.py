import pygame
from pygame.locals import *
from sys import exit
pygame.init()

IMAGE_PATH = 'Menu_UI/'

WIDTH = 1130  #整个框架的宽
HEIGHT = 652
class escmenu_UI(object):
    def __init__(self):
        self.esc_screen=pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        ico = pygame.image.load("UI/my.ico")
        pygame.display.set_icon(ico)  # 可以填img
        pygame.display.set_caption("滑雪大冒险")
        self.i0 = pygame.image.load(IMAGE_PATH +'tool.png')
        self.i1=pygame.image.load(IMAGE_PATH +'继续游戏.png')
        self.i1_click=pygame.image.load(IMAGE_PATH +'继续游戏_大.png')
        self.i3=pygame.image.load(IMAGE_PATH +'返回菜单.png')
        self.i3_click=pygame.image.load(IMAGE_PATH +'返回菜单_大.png')
        self.bg_image=pygame.image.load(IMAGE_PATH +'escmenu.png')
        self.still=False        # 防止跳页时鼠标点击重复生效
        self.n_quitgame=False
        self.esc_save=False
    def escmenu_transform (self):
        #将图片缩放至合适大小
        i0_rect=self.i0.get_rect()
        title_size=(int(i0_rect[2]*3/4),int(i0_rect[3]*3/4))
        self.i0=pygame.transform.scale(self.i0,title_size)
        i_rect=self.i1.get_rect()
        size=(int(i_rect[2]*2/3),int(i_rect[3]*2/3))
        self.i1=pygame.transform.scale(self.i1,size)
        self.i1_click=pygame.transform.scale(self.i1_click,size)
        self.i3=pygame.transform.scale(self.i3,size)
        self.i3_click=pygame.transform.scale(self.i3_click,size)
    def escmenu_select(self):
        clock = pygame.time.Clock()
        self.esc_screen.fill([255, 255, 255])
        n1=True
        while n1:
            for event in pygame.event.get():
            # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:    # 1代表的是鼠标左键
                        still=True
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        n1=False
            clock.tick(30)
            self.esc_screen.blit(self.bg_image,(64,40))
            self.esc_screen.blit(self.i1,(380,150))
            self.esc_screen.blit(self.i3,(380,350))
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1>315 and x1<620 and y1<235 and y1>150:
                self.esc_screen.blit(self.i1_click,(372,155))
                if buttons[0] and still==True:
                    n1=False
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    n1 = False

            elif x1>315 and x1<620 and y1<435 and y1>365:
                self.esc_screen.blit(self.i3_click,(372,355))
                if buttons[0] and still==True:
                    n1=False
                    self.n_quitgame=True
            else:
                self.esc_screen.blit(self.i1,(380,150))
                self.esc_screen.blit(self.i3,(380,350))
            pygame.display.update()