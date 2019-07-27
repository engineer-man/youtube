#!/usr/bin/env python3.7

import sys
import random
import os
import math

COLUMNS = 12
ROWS = 16

os.system('clear')

data = [random.randint(0, 99) for i in range(COLUMNS)]
minimum = min(data)
maximum = max(data)

chart = []

# chart structure
for row in range(ROWS):
    chart.append([])
    chart[row].append(math.ceil((maximum / ROWS) * row))
    for d in data:
        chart[row].append('   ')

for r_idx, row in enumerate(chart):
    for c_idx, col in enumerate(data, start=1):
        if col >= row[0]:
            chart[r_idx][c_idx] = ' _ '

chart.reverse()

for row in chart:
    for col in row:
        sys.stdout.write(f'{str(col).rjust(3)} ')
    sys.stdout.write('\n')

sys.stdout.write('     ')
for d in data:
    sys.stdout.write(f'{str(d).ljust(4)}')
print()
