#!/usr/bin/env python3

from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# Get screen height
image = device.screencap()
with open('screen.png', 'wb') as f:
    f.write(image)
image = Image.open('screen.png')
width, height = image.size
print(f'Screen height is {height} pixels')

# Get first black pixel in 5th column and adding 30px to set control line number
for i in range(0, height):
    pixVal = image.getpixel((4, i))
    if pixVal == (0, 0, 0, 255):
        control_line = i + 30
        print(f'Control line number is {control_line}')
        break

while True:
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)

    pixels = [list(i[:3]) for i in image[control_line]]

    transitions = []
    ignore = True
    black = True

    for i, pixel in enumerate(pixels):
        r, g, b = [int(i) for i in pixel]

        if ignore and (r + g + b) != 0:
            continue

        ignore = False

        if black and (r + g + b) != 0:
            black = not black
            transitions.append(i)
            continue

        if not black and (r + g + b) == 0:
            black = not black
            transitions.append(i)
            continue

    # Sometimes this can cause issues
    try:
        start, target1, target2 = transitions
    except:
        # If there is a problem, just skip this iteration
        continue
    gap = target1 - start
    target = target2 - target1
    distance = (gap + target / 2) * .98

    print(f'transition points: {transitions}, distance: {distance}')

    device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)}')

    time.sleep(min(2.5, 1.1 + (3 * (distance / 1000))))
