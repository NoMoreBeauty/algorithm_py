F={}
def fib(n):
	if n<2:
		return n
	F[n]=fib(n-1)+fib(n-2)
	return F[n]
fib(10)
print(F)
