inputs = open('inputs.txt').read().strip().split('\n')

# puzzle 1
print(sum([int(i) for i in inputs]))

# puzzle 2
seen = set()
f = 0
while True:
    for i in inputs:
        f += int(i)
        if f in seen:
            print(f)
            quit()
        seen.add(f)
