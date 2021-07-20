# -*- coding:utf-8 -*-

import pygame, random
UI = 'UI/'
skier_images = [UI + "skier_down.png", UI + "skier_right1.png", UI + "skier_right2.png",
                UI + "skier_left2.png", UI + "skier_left1.png"]

skier_2_images = [UI + "skier2_down.png", UI + "skier2_right1.png", UI + "skier2_right2.png",
                  UI + "skier2_left2.png", UI + "skier2_left1.png"]

# 滑雪者角色类
class SkierClass(pygame.sprite.Sprite):
    def __init__(self, player_ice):
        pygame.sprite.Sprite.__init__(self)
        if player_ice:  # 使用角色冰墩墩
            self.image = pygame.image.load(UI + "skier_down.png")
        else:  # 使用角色雪熔融
            self.image = pygame.image.load(UI + "skier2_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [552, 100]
        self.angle = 0
        self.MaxSpeed = 10
        self.player_ice = player_ice
        self.combo = 0

    def turn(self, direction):
        # 当滑雪者转向时，加载对应的图片并且修改速度值
        self.angle = self.angle + direction
        if self.angle == -2 or self.angle == 2:
            self.combo +=30                  #左右二段滑可获得combo加分
        if self.angle < -2:  self.angle = -2
        if self.angle > 2:  self.angle = 2
        center = self.rect.center
        if self.player_ice:  # 使用角色冰墩墩
            self.image = pygame.image.load(skier_images[self.angle])
        else:  # 使用角色雪熔融
            self.image = pygame.image.load(skier_2_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, self.MaxSpeed - abs(self.angle) * 2]
        return speed

    def move(self, speed):

        self.rect.centerx = self.rect.centerx + speed[0] * 4
        if self.rect.centerx < 120: #+ 320:
            self.rect.centerx = 120 #+ 320
        if self.rect.centerx > 1050: #+ 320:
            self.rect.centerx = 1050 #+ 320

    def out_mode(self):
        if self.player_ice:  # 使用角色冰墩墩
            self.image = pygame.image.load(skier_images[0])
        else:  # 使用角色雪熔融
            self.image = pygame.image.load(skier_2_images[0])
        self.rect.centery += 2
        if self.rect.centery > 700:
            return 1
        else:
            return 0

    def judge_result(self,points, flag, highspeed, hit, combo, slide):
        if points > 1500 and (flag > 30 or highspeed > 15) and combo > 30 and hit < 5:
            return 1
        elif points > 1000 and (flag > 15 or highspeed > 10) and combo > 20 and hit < 10:
            return 2
        elif points > 500 and (flag > 10 or highspeed > 5) and combo > 10 and hit < 20:
            return 3
        else:
            return 0
    def draw_result(self,medal, screen,result):
        skier_gold_image = pygame.image.load(UI + 'medal_gold.png')
        skier_silver_image = pygame.image.load(UI + 'medal_silver.png')
        skier_copper_image = pygame.image.load(UI + 'medal_copper.png')
        skier_none_image = pygame.image.load(UI + 'medal_none.png')
        skier_back_image = pygame.image.load(UI + 'back_menu.png')

        if result:
            medal.add_medal(result)
        if result == 1:
            screen.blit(skier_gold_image, [270, 220])
        elif result == 2:
            screen.blit(skier_silver_image, [270, 220])
        elif result == 3:
            screen.blit(skier_copper_image, [270, 220])
        else:
            screen.blit(skier_none_image, [270, 220])
        screen.blit(skier_back_image, [280, 320])

    # 表示障碍物的类定义,包括树和旗子
    def end_animation(self,screen):
        clock = pygame.time.Clock()
        if self.player_ice:  # 使用角色冰墩墩
            self.image = pygame.image.load(skier_images[0])
        else:  # 使用角色雪熔融
            self.image = pygame.image.load(skier_2_images[0])
        while self.rect.centery < 640:
            self.rect.centery += 60
            clock.tick(60)
            self.draw(screen)


class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self, speed):
        self.rect.centery -= speed[1]
        if self.rect.centery < -32:
            self.kill()


# 重绘显示区域，形成动画效果
def animate(screen, obstacles, skier, score_text,meter_text):
    screen.fill([255, 255, 255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [30, 10])
    screen.blit(meter_text, [30, 45])
    pygame.display.flip()


def create_map(obstacles):
    i = 0
    locations = []
    for i in range(9):
        row = random.randint(0, 8)
        col = random.randint(0, 9)
        location = [col * 111 + 120 , row * 64 + 32 + 640]
        if not (location in locations):
            locations.append(location)
            type = random.choice(["flag", "flag","flag","flag","barrier","barrier","barrier","ice"])
            if type == "barrier":
                barrier_choice = random.choice([0,1])
                if barrier_choice == 0:
                    img = UI + "skier_barrier_1.png"
                else:
                    img = UI + "skier_barrier_2.png"
            elif type == "flag":
                img = UI + "skier_flag.png"
            elif type == "ice":
                img = UI + "ice_surface.png"
                type = random.choice(["ice","ice_surface"])
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)
    a = 0
    for i in range(5):
        obstacle = ObstacleClass(UI + "skier_side"+str(a)+".png", [9 * 111 + 64 + 48, i * 128 + 32 + 640], "barrier")
        obstacles.add(obstacle)
        obstacle = ObstacleClass(UI + "skier_side"+str(a)+".png", [64 - 32, i * 128 + 32 + 640], "barrier")
        obstacles.add(obstacle)
        a=a+1
        a=a%3


def create_endline(obstacles):
    img = UI + "line.png"
    type = "endline"
    obstacle = ObstacleClass(img, [570,640], type)
    obstacles.add(obstacle)

def create_startline(obstacles):
    img = UI + "line.png"
    type = "startline"
    obstacle = ObstacleClass(img, [570,640], type)
    obstacles.add(obstacle)

def create_fivecircle(obstacles):
    img = UI + "five_circle.png"
    type = "startline"
    obstacle = ObstacleClass(img, [570, 470], type)
    obstacles.add(obstacle)