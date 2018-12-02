inputs = open('inputs.txt').read().strip().split('\n')

twice = 0
thrice = 0

for string in inputs:
    d = {}
    for letter in string:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    for k, v in d.items():
        if v == 2:
            twice += 1
            break
    for k, v in d.items():
        if v == 3:
            thrice += 1
            break

print(twice * thrice)
