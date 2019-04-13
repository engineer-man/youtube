#!/usr/bin/env python3

import sys

start_num = int(sys.argv[1])
count = int(sys.argv[2])

list = []

for i in range(0, count):
    list.append(i * start_num)

sum = 0
divisible = 0

for num in list:
    sum += num
    if num % 10 == 0:
        divisible += 1

print(sum, divisible)
