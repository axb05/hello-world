#coding utf8
#write by axb
#20190216

import pygame

from settings import Settings
from white_ball import White_ball
#from red_ball import Red_ball
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('ball game')

    #播放背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1,1)
    #创建红球
    white_ball = White_ball(ai_settings,screen)
    #创建白球
    #red_balls = Red_ball(ai_settings,screen)
    red_balls = Group()
    #开始主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,white_ball,red_balls)
        # 移动飞船
        gf.update_white_ball(white_ball)
        # 更新子弹位置
        gf.update_red_balls(red_balls)
        # 更新屏幕
        gf.update_screen(ai_settings,screen,white_ball,red_balls)

run_game()
