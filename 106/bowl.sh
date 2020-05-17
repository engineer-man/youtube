#!/usr/bin/env bash

# move ball
adb shell input touchscreen swipe 540 1700 500 1700 400

sleep 1

# throw ball
adb shell input touchscreen swipe 540 1700 540 1400 500
