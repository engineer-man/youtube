# definition
def my_fn():
	# your code
	print 'hello'

# arguments/return
def add(n1, n2):
	return n1 + n2

# multiple return
def square(n1, n2):
	return n1**2, n2**2

# calling
my_fn()
result = add(n2=1, n1=2)
print result
result1, result2 = square(1, 2)
print result1, result2
