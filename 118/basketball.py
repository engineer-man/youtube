#!/usr/bin/env python3

from ppadb.client import Client
import time
import threading

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

ready = False
min_x = 415
shoot_x = None

def monitor_hoop():
    global ready
    global shoot_x

    input('')

    start = time.time()

    while True:
        cycle = 6.25
        delta = time.time() - start
        perc1 = (delta % cycle) / cycle

        dir = 'r' if perc1 < .5 else 'l'

        perc2 = perc1 + .24

        if dir == 'l' and perc2 > 1:
            perc2 = perc2 - 1

        if perc2 > .5:
            perc2 = .5 - (perc2 - .5)

        shoot_x = min_x + perc2 * 2 * 250
        ready = True

        print(shoot_x)

        time.sleep(.005)



t1 = threading.Thread(target=monitor_hoop)
t1.daemon = True
t1.start()

while True:
    if not ready:
        time.sleep(.5)
        continue

    device.shell(f'input touchscreen swipe 540 1600 {int(shoot_x)} 820 300')
