import pygame
from sys import exit
pygame.init()

IMAGE_PATH = 'Menu_UI/'
audios = 'audios/'
UI = 'UI/'

WIDTH = 1130  #整个框架的宽
HEIGHT = 652
class Mainmenu_UI(object):
    def __init__(self):
        self.Main_screen= pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        ico = pygame.image.load("UI/my.ico")
        pygame.display.set_icon(ico)  # 可以填img
        pygame.display.set_caption("滑雪大冒险")
        self.i0=pygame.image.load(IMAGE_PATH +'title.png')
        self.i1=pygame.image.load(IMAGE_PATH +'开始游戏.png')
        self.i1_click=pygame.image.load(IMAGE_PATH +'开始游戏_大.png')
        self.i2=pygame.image.load(IMAGE_PATH +'勋章墙.png')
        self.i2_click=pygame.image.load(IMAGE_PATH +'勋章墙_大.png')
        self.i3=pygame.image.load(IMAGE_PATH +'退出游戏.png')
        self.i3_click=pygame.image.load(IMAGE_PATH +'退出游戏_大.png')
        self.i7=pygame.image.load(IMAGE_PATH +'player_choose_1.png')
        self.i8=pygame.image.load(IMAGE_PATH +'player_choose_2.png')
        self.i9 = pygame.image.load(IMAGE_PATH + 'player_choose.png')

        self.frame = pygame.image.load(UI + '边框.png')
        self.bg_image=pygame.image.load(IMAGE_PATH +'background.png')
        self.Mainmenu_sound = pygame.mixer.Sound(audios + "Mainmenu_begin.wav")

        self.volume=1
        self.still=False        # 防止跳页时鼠标点击重复生效
        self.n_return=False
        self.n_medalWall = False  #进入勋章墙
        self.n_game = False
        self.n_ice = False  #True为雪容融，False为冰墩墩
        self.isAI = False
        self.n_loadgame = False
    def Mainmenu_transform (self):
        #将图片缩放至合适大小
        i0_rect=self.i0.get_rect()
        title_size=(int(i0_rect[2]*3/4),int(i0_rect[3]*3/4))
        self.i0=pygame.transform.scale(self.i0,title_size)
        i_rect=self.i1.get_rect()
        size=(int(i_rect[2]*2/3),int(i_rect[3]*2/3))
        self.i1=pygame.transform.scale(self.i1,size)
        self.i1_click=pygame.transform.scale(self.i1_click,size)
        self.i2=pygame.transform.scale(self.i2,size)
        self.i2_click=pygame.transform.scale(self.i2_click,size)
        self.i3=pygame.transform.scale(self.i3,size)
        self.i3_click=pygame.transform.scale(self.i3_click,size)
        self.Main_screen.fill((255,255,255))

    def Mainmenu_select (self):
        #菜单选择
        self.Mainmenu_sound.set_volume(self.volume)
        self.Mainmenu_sound.play(0)
        clock = pygame.time.Clock()
        n1=True
        n2=True
        # 第一次循环，判断开始游戏、勋章墙和退出游戏
        while n1:
            for event in pygame.event.get():
            # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:    # 1代表的是鼠标左键
                        still=True

            clock.tick(30)
            self.Main_screen.blit(self.bg_image,(0,0))
            self.Main_screen.blit(self.i0,(0,0))
            self.Main_screen.blit(self.i1,(150,150))
            self.Main_screen.blit(self.i2,(150,300))
            self.Main_screen.blit(self.i3,(150,450))
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()

            if x1>165 and x1<490 and y1<235 and y1>150:
                self.Main_screen.blit(self.i1_click,(150,150))
                if buttons[0] and still==True:
                    n1 = False
                    self.n_game = True
            elif x1>165 and x1<470 and y1<385 and y1>290:
                self.Main_screen.blit(self.i2_click,(150,300))
                if buttons[0] and still==True:
                    n1 = False
                    n2 = False
                    self.n_medalWall = True
            elif x1>165 and x1<490 and y1<535 and y1>465:
                self.Main_screen.blit(self.i3_click,(150,450))
                if buttons[0] and still==True:
                    pygame.quit()
                    exit()
            else:
                self.Main_screen.blit(self.i1,(150,150))
                self.Main_screen.blit(self.i2,(150,300))
                self.Main_screen.blit(self.i3,(150,450))
            pygame.display.update()
        still=False

        #第二次循环，选择冰墩墩或雪容融
        while n2:

            for event in pygame.event.get():
                # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:    # 1代表的是鼠标左键
                        still=True
            clock.tick(30)
            self.Main_screen.blit(self.bg_image,(0,0))
            self.Main_screen.blit(self.i9,(120,75))
            buttons3 = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()

            if x1>=242 and x1<=534 and y1<476 and y1>274:
                self.Main_screen.blit(self.i7,(120,75))
                if buttons3[0] and still==True:
                    n2=False
                    self.n_ice = True
            elif x1>610 and x1<907 and y1<476 and y1>274:
                self.Main_screen.blit(self.i8,(120,75))
                if buttons3[0] and still==True:
                    n2=False

            else:
                self.Main_screen.blit(self.i9,(120,75))
                pass
            pygame.display.update()
        self.Mainmenu_sound.stop()

pygame.quit()