#!/usr/bin/env bash

echo -e "\xA0\x01\x01\xA2" > /dev/ttyUSB0
sleep .5
echo -e "\xA0\x01\x00\xA1" > /dev/ttyUSB0
