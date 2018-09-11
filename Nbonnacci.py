import math as m
def Nbonacci(n,N):
	"""IN THE Nbonnaci fuction:
	n -- How many numbers you want in the sequence
	N -- The factor for generating the sequence"""
	if n == 0:
		print("The numbers in a N-bonnacci Sequence should be greater than 2")
		print("Cannot find ratio with no Sequence")
	
	elif n == 1:
		print("The numbers in a N-bonnacci Sequence should be greater than 2")
		print("Cannot find ratio with one value")
		return l
		
		
	elif n == 2:
		print("The numbers in a N-bonnacci Sequence should be greater than 2")
		print("Cannot find ratio with two values")
		return l
		
	elif n > 2:
		ratio = 0
		l  = [0,1]
		for i in range(2, n):
			p = (N*l[len(l)-1]) + l[len(l)-2]
			l.insert(len(l), p )
			l.sort()
			i = i+1
			ratio = l[len(l)-1]/l[len(l)-2]
		return l
		return ratio
	
