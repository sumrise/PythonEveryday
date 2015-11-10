#!python2.7
# coding=UTF-8

# info TODO

__author__ = 'sumrise'

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 设置字体
font = ImageFont.truetype("/Library/Fonts/Arial Italic.ttf", 20)


imageFile = "head.png"
im1 = Image.open(imageFile)
draw = ImageDraw.Draw(im1)
draw.text((350, 20), "10", (255, 0, 0), font=font)
draw = ImageDraw.Draw(im1)

im1.save("target.png")
