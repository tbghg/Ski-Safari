import pygame
from pygame.locals import *
from sys import exit
# SAVE_PATH = 'savedata/'
UI = 'UI/'
Medal_path = 'medal_data/'

left_side = 75
up_side = 85
level_interval = 250  #  水平 间隔
vertical_interval = 250  #  竖直 间隔
wide = 1130
high = 652
PIC_wide = 200
PIC_high = 200
POST = [(left_side + level_interval*0, up_side),(left_side + level_interval*1, up_side),(left_side + level_interval*2, up_side),(left_side + level_interval*3, up_side),(left_side + level_interval*0, up_side+vertical_interval),(left_side + level_interval*1, up_side+vertical_interval),(left_side + level_interval*2, up_side+vertical_interval),(left_side + level_interval*3, up_side+vertical_interval)]
POST_RECT = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
hover_medal = [False, False, False, False, False, False, False, False]

for i in range(8):
    POST_RECT[i][0] = POST[i][0]
    POST_RECT[i][1] = POST[i][0] + PIC_wide
    POST_RECT[i][2] = POST[i][1]
    POST_RECT[i][3] = POST[i][1] + PIC_high

class medal_Wall(object):
    def __init__(self):
        pygame.init()
        self.Page_Max = 1
        self.page = 1
        self.sum = 0
        self.next = True
        self.medal_list = []
        self.i_shelf = pygame.image.load(UI + 'medal_shelf.png')
        self.i_shelf = pygame.transform.scale(self.i_shelf, (wide, high+30))
        self.__screen = pygame.display.set_mode((wide, high), 0, 0)
        self.__screen.fill([255, 255, 255])

    def medal_show(self):  # 把文档里的图片全部给贴上
        self.Read_Medal()
        for i in range(8):
            self.__screen.blit(self.i_shelf, (0, -30))
            self.Pic = pygame.image.load(UI + str(self.medal_list[self.page*8 - 8 + i]) + '.png')
            self.__screen.blit(self.Pic, POST[i])
            pygame.display.update()
        if self.page != self.Page_Max:  # 说明还有下一页！！！
            self.Pic0 = pygame.image.load(UI + 'next.png')
        else:
            self.next = False
            self.Pic0 = pygame.image.load(UI + 'no_next.png')
        self.__screen.blit(self.Pic0, (wide - 105, high - 105))
        pygame.display.update()

    def Load_Game__Mouse(self):
        self.medal_show()
        clock = pygame.time.Clock()  # 画一下初始的红色方框
        clock.tick(60)
        loop = True
        self.page = 1
        self.next = True
        while loop:
            if self.page == self.Page_Max:
                self.next = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loop = False
            buttons = pygame.mouse.get_pressed()  # 检测鼠标按的状态
            x1, y1 = pygame.mouse.get_pos()  # 获取鼠标位置
            for i in range(8):
                if POST_RECT[i][0] <= x1 <= POST_RECT[i][1] and POST_RECT[i][2] <= y1 <= POST_RECT[i][3]:  # 检测鼠标位置
                    self.Pic = pygame.image.load(UI + str(self.medal_list[self.page * 8 - 8 + i]) + '_.png')
                    self.__screen.blit(self.Pic, POST[i])
                    pygame.display.update()
                else:
                    self.Pic = pygame.image.load(UI + str(self.medal_list[self.page * 8 - 8 + i]) + '.png')
                    self.__screen.blit(self.Pic, POST[i])
                    pygame.display.update()

            if wide - 100 <= x1 <= wide-50 and high - 100 <= y1 <= high-50 and self.next:  # 下一页（属于瞎写状态）
                #pygame.draw.rect(self.__screen, [255, 0, 0], [wide - 107, high - 100, 50, 60], 3)  # 画方框
                self.Pic = pygame.image.load(UI + "next_b.png")
                self.__screen.blit(self.Pic, (wide - 105, high - 105))
                pygame.display.update()
                if buttons[0] :
                    self.page += 1
                    self.__screen.fill([255, 255, 255])
                    self.__screen.blit(self.i_shelf, (70, 150))
                    self.medal_show()
            else:
                self.__screen.blit(self.Pic0, (wide - 105, high - 105))

    def add_medal(self, medal):     #   添加奖章的接口
        if medal:                   #  如果有奖章1为金，类推
    #        fl = open(SAVE_PATH + "medal.txt", "a")
            fl = open(Medal_path + "medal.txt", "a")
            fl.write(str(medal) + '\n')
            fl.close()

    def Read_Medal(self):
        self.medal_list = []
    #    fl = open(SAVE_PATH + "medal.txt", "r")
        fl = open(Medal_path + "medal.txt", "a")
        fl.close()
        fl = open(Medal_path + "medal.txt", "r")
        lines = fl.readlines()
        for msg in lines:
            msg = msg.strip('\n')
            self.medal_list.append(int(msg))
        fl.close()
        self.sum = len(self.medal_list)
        if self.sum == 0:
            self.medal_list = [0,0,0,0,0,0,0,0]
        else:
            self.Page_Max = int((self.sum-1)/8)+1   #总共有几页
            temp = 8 - self.sum % 8
            for i in range(temp):
                self.medal_list.append(0)