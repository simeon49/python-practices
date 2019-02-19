#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 官方: https://pillow.readthedocs.io/en/stable/

#  PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，
# 支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

# pip install pillow

import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter

###################################################
#  生成字母验证码
###################################################

width = 60 * 4
height = 60

# 240 * 60
image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
# Font
font = ImageFont.truetype('Arial.ttf', size=36)
# 画布
draw = ImageDraw.Draw(image)

# 绘制背景
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)))

# 绘制字母
for t in range(4):
    ch = chr(random.randint(65, 90))
    draw.text((60 * t + 10, 10), text=ch, fill=(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)), font=font)

# 模糊
image = image.filter(ImageFilter.BLUR)

image.save('code.jpg', 'jpeg')
