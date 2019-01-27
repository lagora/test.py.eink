#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import os

text = os.environ['TEXT']
print('text', text)
font = './RobotoMono-Regular.ttf'
epd = epd2in13b.EPD()
epd.init()
epd.Clear()
HBlackimage = Image.new('1', (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)  # 298*126
HRedimage = Image.new('1', (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)  # 298*126
drawblack = ImageDraw.Draw(HBlackimage)
drawred = ImageDraw.Draw(HRedimage)
font20 = ImageFont.truetype(font, 20)
drawblack.text((0, 0), text, font = font20, fill = 0)
epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
epd.sleep()
