import Levenshtein

inputs = open('inputs.txt').read().strip().split('\n')

ratios = []

for i1 in inputs:
    for i2 in inputs:
        ratios.append('{}: {}/{}'.format(Levenshtein.ratio(i1, i2), i1, i2))

result = sorted([i for i in ratios if not i.startswith('1.0')])[-1]
strings = result.split(': ')[1].split('/')
s1 = strings[0]
s2 = strings[1]

final = ''

for i in range(0, len(s1)):
    if s1[i] == s2[i]:
        final += s1[i]

print(final)
