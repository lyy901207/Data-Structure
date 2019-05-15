
def fibonacci(n):
	a, b = 0, 1
	if n == 1: return a
	if n == 2: return b
	i = 1
	while i < n:
		a, b = b, a+b
		i += 1
	return a

def fib2(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fib2(n-1) + fib2(n-2)



if __name__=='__main__':
	print(fib2(5), fibonacci(5))