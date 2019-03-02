def fab(max): 
	n, a, b = 0, 0, 1 
	while n < max: 
		yield b 
		# print b 
		a, b = b, a + b 
		n = n + 1 

a = fab(10)
while 1:
	try:
		print a.next()
	except StopIteration, e:
		print 'Error'
		break

