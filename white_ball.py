#coding utf8
#axb
#20190216

import pygame

class White_ball():
    """白球信息"""

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #加载图片
        self.image = pygame.image.load(self.ai_settings.white_ball_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)  # self.rect.centerx设置不了浮点数 只能另设置一个变量进行运算
        self.bottomy = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制白球"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        # 向右移动飞船
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.white_ball_speed_factor
        # 向左移动飞船
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.white_ball_speed_factor

        self.rect.centerx = self.centerx

        if self.moving_up and self.rect.top > 0:
            self.bottomy -= self.ai_settings.white_ball_speed_factor
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.bottomy += self.ai_settings.white_ball_speed_factor

        self.rect.bottom = self.bottomy
