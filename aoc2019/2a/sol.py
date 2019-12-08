#!/usr/bin/env python3

import math

total = 0

numbers = [int(i) for i in open('input.txt').read().strip().split(',')]
numbers[1] = 12
numbers[2] = 2

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

print(numbers[0])
