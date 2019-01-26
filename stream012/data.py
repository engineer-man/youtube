import csv

with open('data.csv') as f:
    #rows = csv.reader(f)
    rows = csv.DictReader(f)
    rows = [row for row in rows]

#print(rows)

sum = 0
sums = {
    'East': 0,
    'West': 0,
    'Central': 0
}
for row in rows:
    sums[row['Region']] += int(row['Units'])
    if row['Region'] == 'Central':
        sum += int(row['Units'])

print(sums)
