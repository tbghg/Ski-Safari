from My_class import *
from Mainmenu import *
from medal_Wall import *
import time
from escmenu import *
import pygame
from sys import exit
pygame.init()

n0=True
n_esc=False
Mainmenu_flag = True

WIDTH = 1130  #整个框架的宽
HEIGHT = 652

UI = 'UI/'
audios = 'audios/'

while n0:

    if Mainmenu_flag==True:
        Select = Mainmenu_UI()
        Select.Mainmenu_transform()
        Select.Mainmenu_select()
        if Select.n_return==True:
            Select.Mainmenu_sound.stop()
            continue
        Medal = medal_Wall()
    if Select.n_game == True:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        ico = pygame.image.load("UI/my.ico")
        pygame.display.set_icon(ico)  # 可以填img
        pygame.display.set_caption("滑雪大冒险")
        pygame.display.flip()
        if Select.n_ice == True:
            player_ice = True  #   角色是不是冰墩墩
        else:
            player_ice = False
        if __name__ == '__main__':

            clock = pygame.time.Clock()
            font = pygame.font.Font('Fonts\consolab.ttf', 30)
            obstacles = pygame.sprite.Group()
            skier = SkierClass(player_ice)  # 里面放参数，True是冰墩墩，Flase是雪熔融
            speed = [0, skier.MaxSpeed]  # 速度值，包含方向与向下的速度
            map_position = 0
            points = 0
            UP = 0
            meters = 0   #控制总里程
            miles = 0
            flags = 0    #记录夺旗数，可做比赛要求
            amount_combo = 0
            amount_flag = 0
            amount_highspeed = 0
            amount_hit = 0
            amount_slide = 0
            n_start_1 = False
            n_end = False
            n_end_start = False
            n_end_end = False
            n_uncontrol = 0
            # 事件处理循环
            running = True
            Playing_sound = pygame.mixer.Sound(audios + "playing_bgm.wav")
            Playing_sound.set_volume(0.2)
            Playing_sound.play(0)
            Hit_sound = pygame.mixer.Sound(audios + "Hit_bgm.wav")
            Hit_sound.set_volume(0.2)
            Flag_sound = pygame.mixer.Sound(audios + "Flag_bgm.wav")
            Flag_sound.set_volume(0.5)
            Ice_sound = pygame.mixer.Sound(audios + "Ice_bgm.wav")
            Ice_sound.set_volume(0.2)

        esc_select = escmenu_UI()

        while running:

            if n_start_1 == False:
                for i in range(3):
                    screen.fill([255, 255, 255])
                    create_fivecircle(obstacles)
                    screen.blit(skier.image, skier.rect)
                    create_startline(obstacles)
                    obstacles.draw(screen)
                    count_down = pygame.image.load(UI + 'count_down_' + str(3 - i) + '.png')
                    #count_down = font.render(str(3 - i), 10, (0, 0, 0))  # 更新提示的文本信息
                    screen.blit(count_down, [0, 0])
                    pygame.display.update()
                    time.sleep(1)

            if map_position >= 640 and not n_end:
                #skier.MaxSpeed += 1
                if UP >= 30:     # 保持高速运动可加分
                    points += 100
                    amount_highspeed +=1
                if miles <=34:
                    create_map(obstacles)
                    meters += 20
                elif miles > 34:
                    create_endline(obstacles)
                map_position = 0
                miles += 1

            map_position += speed[1]  # 修改地图的位置，使得障碍物向上移动，造成了滑雪者向下滑行的效果
            hit = pygame.sprite.spritecollide(skier, obstacles, False)

            if hit:
                if hit[0].type == "barrier" and not hit[0].passed:  # 碰到了障碍，并且这个障碍还没有被“处理”过
                    Hit_sound.play(0)
                    points = points - 100
                    amount_hit +=1
                    if player_ice:
                        skier.image = pygame.image.load(UI + "skier_crash.png")  # 显示滑雪者翻倒的图片
                    else:
                        skier.image = pygame.image.load(UI + "skier2_crash.png")  # 显示滑雪者翻倒的图片
                    animate(screen, obstacles, skier, score_text,meter_text)
                    pygame.time.delay(1000)
                    if player_ice:
                        skier.image = pygame.image.load(UI + "skier_down.png")  # 显示滑雪者正常滑行的图片
                    else:
                        skier.image = pygame.image.load(UI + "skier2_down.png")  # 显示滑雪者正常滑行的图片
                    skier.angle = 0
                    skier.MaxSpeed = 10
                    UP = 0
                    speed = [0, skier.MaxSpeed]
                    hit[0].passed = True
                elif hit[0].type == "flag" and not hit[0].passed:  # 碰到了一个旗子
                    Flag_sound.play(0)
                    points += 30
                    amount_flag +=1
                    hit[0].kill()  # 清除点这个被碰到的旗子
                elif hit[0].type == "ice":
                    Ice_sound.play(0)
                    direct = random.choice([-1,1])
                    speed = skier.turn(direct)
                    n_uncontrol = 50
                    amount_slide += 1
                elif hit[0].type == "ice_surface":
                    #direct = random.choice([-2, 2])
                    #speed = skier.turn(direct)
                    Ice_sound.play(0)
                    UP += 1
                    n_uncontrol = 70
                    amount_slide += 1
                elif hit[0].type == "endline":
                    n_end = True    # 结束游戏
            if not n_end:
                obstacles.update(speed)
                #meters += 0.5

            score_text = font.render("Score: " + str(points), 1, (0, 0, 0))  # 更新提示的文本信息
            meter_text = font.render("Meters: " + str(meters) + 'm', 1, (0, 0, 0))  # 更新提示的文本信息

            animate(screen, obstacles, skier, score_text,meter_text)

            clock.tick(60 + UP)  # 设定每秒帧数
            UP += 0.05
            n_uncontrol -=1
            if n_uncontrol < 0:
                n_uncontrol = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN and (not n_uncontrol) and(not n_end):  # 如果按下了键盘上的键
                    if event.key == pygame.K_LEFT:  # 如果按下了向左的方向键
                        speed = skier.turn(-1)
                        if skier.combo:
                            points +=skier.combo        #左右二段滑可获得combo加分
                            amount_combo +=1
                            skier.combo = 0

                    elif event.key == pygame.K_RIGHT:  # 如果按下了向右的方向键
                        speed = skier.turn(1)
                        if skier.combo:
                            points += skier.combo  # 左右二段滑可获得combo加分
                            amount_combo += 1
                            skier.combo = 0
                    #elif event.key == pygame.K_DOWN:  # 如果按下了向左的方向键
                        # UP = UP + 5

                    elif event.key == pygame.K_UP:  # 如果按下了向右的方向键
                        if UP <= 0:
                            continue
                        else:
                            UP = UP - 5
                    elif event.key == pygame.K_ESCAPE:
                        n_esc = True
            skier.move(speed)  # 滑雪者向左或向右移动
            if n_esc:
                esc_select = escmenu_UI()
                esc_select.escmenu_transform()
                esc_select.escmenu_select()
                n_esc = False
            if esc_select.n_quitgame ==True:
                break

            n_start_1 = True

            if n_end == True:
                n_end_start = True

            if n_end_start == True:
                speed[0] = 0
                if(skier.out_mode() == 1):
                    n_end_end = True

            if n_end_end == True:
               # skier.end_animation(screen)
                result = skier.judge_result(points, amount_flag, amount_highspeed, amount_hit, amount_combo, amount_slide)

                skier.draw_result(Medal,screen,result)
                pygame.display.update()
                running = False
                end_press = True
                while end_press:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                            end_press = False

    elif Select.n_medalWall == True:
        Medal.Load_Game__Mouse()
    try:
        Playing_sound.stop()
    except:
        pass

pygame.quit()  # 退出pygame