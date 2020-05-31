#!/usr/bin/env python3

from ppadb.client import Client
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

device.shell('input tap 532 957')

time.sleep(.5)

g = { 'left': 2750, 'top': 1790, 'width': 1, 'height': 1 }
y = { 'left': 2750, 'top': 2500, 'width': 1, 'height': 1 }
r = { 'left': 3120, 'top': 1790, 'width': 1, 'height': 1 }
b = { 'left': 3120, 'top': 2500, 'width': 1, 'height': 1 }

sct = mss()

def detect_next():
    detecting = False

    while True:
        time.sleep(.1)

        green_pixel = numpy.array(sct.grab(g))
        yellow_pixel = numpy.array(sct.grab(y))
        red_pixel = numpy.array(sct.grab(r))
        blue_pixel = numpy.array(sct.grab(b))

        green_r = green_pixel[0][0][2]
        yellow_r = yellow_pixel[0][0][2]
        red_r = red_pixel[0][0][2]
        blue_r = blue_pixel[0][0][2]

        if not detecting and \
            green_r > 10 and \
            yellow_r > 10 and \
            red_r > 10 and \
            blue_r > 10:
            detecting = True

        if not detecting:
            continue

        if 1 <= green_r <= 10:
            return 'g'
        if 1 <= yellow_r <= 10:
            return 'y'
        if 1 <= red_r <= 10:
            return 'r'
        if 1 <= blue_r <= 10:
            return 'b'

moves = 1
colors = []

while True:
    for i in range(moves):
        color = detect_next()
        print(f'detected {color}')

        colors.append(color)

    print(colors)

    time.sleep(1)

    for color in colors:
        if color == 'g':
            device.shell('input tap 300 450')
        if color == 'y':
            device.shell('input tap 300 1450')
        if color == 'r':
            device.shell('input tap 800 450')
        if color == 'b':
            device.shell('input tap 800 1450')

    moves += 1
    colors = []
