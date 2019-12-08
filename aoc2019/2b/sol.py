#!/usr/bin/env python3

import math

total = 0

orig_numbers = [int(i) for i in open('input.txt').read().strip().split(',')]

for x in range(100):
    for y in range(100):
        numbers = orig_numbers[:]
        numbers[1] = x
        numbers[2] = y
        i = 0
        while i < len(numbers):
            if numbers[i] == 99:
                break
            if numbers[i] == 1:
                numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
                i += 4
                continue
            if numbers[i] == 2:
                numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
                i += 4
                continue
        if numbers[0] == 19690720:
            print(x, y)
            quit()
