from heapq import *
def dispatch(A):
	sum=0
	C={}
	B=list(A.keys())
	for i in range(len(B)):
		temp=A[B[i]]/B[i]
		C[temp]=A[B[i]]
		B[i]=temp
	heapify(B)
	wait=0
	while len(B)>0:
		t=heappop(B)
		sum+=C[t]*(1/t*C[t]+wait)
		wait+=1/t*C[t]
	return sum
print(dispatch({4:2,5:4}))
