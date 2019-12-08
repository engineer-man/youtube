#!/usr/bin/env python3

import math

total = 0

numbers = open('input.txt').read().strip().split('\n')

for number in numbers:
    while True:
        number = math.floor(int(number) / 3) - 2
        if number <= 0:
            break
        total += number

print(total)
