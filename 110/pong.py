import cv2
import numpy as np
from PIL import Image
import mss
from ppadb.client import Client
import threading

paddle_x = 1700 # stays constant
paddle_y = 540
paddle_y_min = 160
paddle_y_max = 920
ball_y = 0

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

running = True
def move_paddle():
    global paddle_y

    while running:
        to = ball_y * 2

        if ball_y < paddle_y_min:
            to = paddle_y_min
        if ball_y > paddle_y_max:
            to = paddle_y_max

        x1 = paddle_x
        y1 = paddle_y
        x2 = paddle_x
        y2 = to

        device.shell(f'input touchscreen swipe {x1} {y1} {x2} {y2} 10')

        paddle_y = to

t = threading.Thread(target=move_paddle)
t.start()

sct = mss.mss()

while True:
    scr = sct.grab({
        'left': 2560,
        'top': 1470,
        'width': 910,
        'height': 540
    })

    img = np.array(scr)

    cv2.rectangle(img, (420, 70), (480, 180), (0,0,0), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT,
        1, 20,
        param1=50, param2=30,
        minRadius=1, maxRadius=40)

    if circles is not None:
        circles = np.uint16(circles)

        for pt in circles[0, :]:
            x, y, r = pt[0], pt[1], pt[2]
            cv2.circle(img, (x, y), r, (0, 0, 255), 5)
            ball_y = y

    cv2.imshow('output', img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break
