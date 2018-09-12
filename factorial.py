def factorial(n):
	f = 1
	if n == 0:
		f = 1
	else:
		for i in range(1, n+1):
			f = f*i
			i += 1
	return f
		
