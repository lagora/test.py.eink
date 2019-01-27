#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from flask import Flask, request

app = Flask(__name__)

font = './RobotoMono-Regular.ttf'
epd = epd2in13b.EPD()
epd.init()
epd.Clear()

'''
HBlackimage = Image.new('1', (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)  # 298*126
HRedimage = Image.new('1', (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)  # 298*126
drawblack = ImageDraw.Draw(HBlackimage)
drawred = ImageDraw.Draw(HRedimage)
font20 = ImageFont.truetype(font, 20)
drawblack.text((0, 0), 'server started', font = font20, fill = 0)
epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
'''

def printOnScreen(text, x = 0, y = 0):
    print("writing", text, x, y)
    # Drawing on the Horizontal image
    epd.Clear()
    HBlackimage = Image.new('1', (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)  # 298*126
    HRedimage = Image.new('1', (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)  # 298*126
    drawblack = ImageDraw.Draw(HBlackimage)
    drawred = ImageDraw.Draw(HRedimage)
    font20 = ImageFont.truetype(font, 20)
    drawblack.text((0, 0), text, font = font20, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/display', methods=['GET', 'POST'])
def display():
    text = request.form['text'] if request.method == 'POST' else request.args.get('text', '')
    printOnScreen(text)
    return 'ok'

if __name__ == "__main__":
    app.run()
