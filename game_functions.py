#coding utf8
#axb
#20190216

import sys
import pygame
from red_ball import Red_ball
import math

def check_events(ai_settings,screen,white_ball,red_balls):
    #监视键盘和鼠标事件

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #调用exit()退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,white_ball,red_balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,white_ball)
        else:
            pass

def update_screen(ai_settings,screen,white_ball,red_balls):
    """更新屏幕"""
    screen.fill(ai_settings.bg_color)
    white_ball.blitme()

    # 循环子弹组里面的元素，进行绘制 为空时不执行
    for red_ball in red_balls.sprites():
        red_ball.draw_red_ball()  # 绘制子弹
    #red_balls.blitme()

    pygame.display.flip()


def check_keydown_events(event,ai_settings,screen,white_ball,red_balls):
    if event.key == pygame.K_RIGHT:
        white_ball.moving_right = True
    elif event.key == pygame.K_LEFT:
        white_ball.moving_left = True
    elif event.key == pygame.K_UP:
        white_ball.moving_up = True
    elif event.key == pygame.K_DOWN:
        white_ball.moving_down = True
    elif event.key == pygame.K_a:
        add_red_ball(ai_settings, screen, white_ball,red_balls)

def check_keyup_events(event,white_ball):
    if event.key == pygame.K_RIGHT:
        white_ball.moving_right = False
    elif event.key == pygame.K_LEFT:
        white_ball.moving_left = False
    elif event.key == pygame.K_UP:
        white_ball.moving_up = False
    elif event.key == pygame.K_DOWN:
        white_ball.moving_down = False

def update_white_ball(white_ball):
    white_ball.update()


def update_red_balls(red_balls):
    '''更新红球位置，'''
    red_balls.update()     # 红球组每个成员执行self.update()操作
    for red_ball in red_balls.sprites():
        pass

    #    if red_ball.rect.bottom <= 0:  # 子弹出界 删除
    #        bullets.remove(bullet)

def add_red_ball(ai_settings,screen,white_ball,red_balls):
    # 创建一个红球对象 加入到红球组
    #print("add red ball")
    #print(len(red_balls))
    if len(red_balls) < ai_settings.red_balls_allowed:  # 红球少于允许值时再生成
        #print(ai_settings.red_balls_allowed)
        new_red_ball = Red_ball(ai_settings, screen, white_ball)
        #print("add to group")
        red_balls.add(new_red_ball)

def collision_red_ball(red_ball_1,red_ball_2):
    """实现两球的碰撞检测"""

    #TODO：1、实现红球碰撞功能；2、改写白球代码，实现红球与白球的碰撞

    tangalpha = (red_ball_2.Rect.centery - red_ball_1.Rect.centery)/(red_ball_2.Rect.centerx - red_ball_1.Rect.centerx)
    alpha = math.atan(tangalpha)
    v1n = red_ball_1.velx * math.cos(alpha) + red_ball_1.vely * math.sin(alpha)
    v2n = red_ball_2.velx * math.cos(alpha) + red_ball_2.vely * math.sin(alpha)
    v1t = red_ball_1.velx * math.sin(alpha) + red_ball_1.vely * math.cos(alpha)
    v2t = red_ball_2.velx * math.sin(alpha) + red_ball_2.vely * math.cos(alpha)
    newv1n = v2n
    newv2n = v1n
    newv1t = v1t
    newv2t =v2t
    red_ball_1.velx = newv1n * math.sin(alpha) + newv1t * math.cos(alpha)
    red_ball_1.vely = newv1n * math.cos(alpha) + newv1t * math.sin(alpha)
    red_ball_2.velx = newv2n * math.sin(alpha) + newv2t * math.cos(alpha)
    red_ball_2.vely = newv2n * math.cos(alpha) + newv2t * math.sin(alpha)