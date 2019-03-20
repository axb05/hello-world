#coding utf-8
#write by axb
#20190216

#从jpg生成png。图片原始大小416*416，缩放为52*52。并且增加透明通道。
# ，白球的图片是找来的。红球的图片是通过PIL库，将它转为RGBA模式后，分为四个通道，再新建一张相同大小的黑色图片，取出其G和B通道，混合后就成为一张红球：

from PIL import Image

orgin_ball = Image.open('images/ball.jpg')

ball_resize = orgin_ball.resize((52,52))

white_img = ball_resize.convert("RGBA")

white_img.save("images/white_ball.png", 'png')

bands = white_img.split()

black_img = Image.new("RGBA", white_img.size, (0, 0, 0))
other_bands = black_img.split()

red_ball = Image.merge("RGBA", (bands[0], other_bands[1], other_bands[2], bands[3]))
red_ball.save("images/red_ball.png", 'png')

