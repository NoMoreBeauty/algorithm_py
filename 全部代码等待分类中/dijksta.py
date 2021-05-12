from heapq import *
def find_min(A,B):
	T=heappop(A)
	index=0
	for i in range(len(B)):
		if B[i]==T:
			index=i
	return index,T
def Dijkstra(A):
	S=[0]
	arr=A[0][:]
	tarr=A[0][1:]
	heapify(tarr) #优先队列（堆）
	while len(S)<5:
		T,temp=find_min(tarr,A[0])
		S.append(T)
		for i in range(len(A[T])):
			if temp+A[T][i]<arr[i] and i not in S:
				arr[i]=temp+A[T][i]
			if arr[i]==100 and A[T][i]!=100 and i not in S:
				arr[i]=t+A[T][i]
	return arr
A=[[0,2,3,5,100],[100,0,2,100,100],[100,100,0,1,100],[100,100,100,0,2],[100,100,100,0,100]]
x=Dijkstra(A)
print(x)