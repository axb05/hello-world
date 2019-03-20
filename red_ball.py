#coding utf8

import pygame
import random
from pygame.sprite import Sprite
import time

class Red_ball(Sprite):


    def __init__(self, ai_settings, screen,white_ball):
        super(Red_ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图片
        self.image = pygame.image.load(self.ai_settings.red_ball_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = random.randint(self.rect.width / 2, self.screen_rect.width - self.rect.width / 2)   #float(self.rect.centerx)  # self.rect.centerx设置不了浮点数 只能另设置一个变量进行运算
        self.centery = random.randint(self.rect.height / 2, self.screen_rect.height - self.rect.height / 2)    #float(self.rect.centery)

        self.velx = random.randint(3, 20) #10
        self.vely = random.randint(3, 20) #8
        self.dt =0.1 #0.01

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def draw_red_ball(self):
        """在指定位置绘制红球"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        self.centerx += self.velx * self.dt
        if self.centerx < self.rect.width / 2 or self.centerx > self.screen_rect.width - self.rect.width / 2:
            self.velx = self.velx * -1

        if self.centery < self.rect.height / 2 or self.centery > self.screen_rect.height - self.rect.height / 2:
            self.vely =self.vely * -1

        self.centery += self.vely * self.dt

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery