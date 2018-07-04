# open/open modes
animals = open('animals.txt', 'a+')
# r  = open for read (default)
# w  = open for write, truncate
# r+ = open for read/write
# w+ = open for read/write, truncate
# a+ = open for read/append

# read
text = animals.read()
print text
animals.seek(0)

# read lines
for animal in animals:
	print animal,

# write/append
animals.write('elephant\n')
animals.write('frog\n')

# close
animals.close()
