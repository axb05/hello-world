#conding utf8
#axb
#20190216

#ball_game游戏中的全局设置保存在此文件中

class Settings():
    """定义一个类，用于存储游戏中的全局设置"""
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (200,200,230) #背景色

        self.white_ball_path = 'images/white_ball.png' #图片路径
        self.white_ball_speed_factor = 1.6

        self.red_ball_path = 'images/red_ball.png' #图片路径
        self.red_balls_allowed = 5

