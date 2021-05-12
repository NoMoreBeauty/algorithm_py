def find(A,V):
	t=100
	index=0
	for i in range(len(A)):
		if A[i]!=-1 and A[i]!=0 and A[i]<t and i not in V:
			t=A[i]
			index=i
	return t,index
def prim(A):
	V=[]
	Narr=A[0]
	V.append(0)
	sum=0
	while len(V)<5:
		t,index=find(Narr,V)
		# print(V)
		print(Narr)
		sum+=t
		print(t)
		V.append(index)
		for i in range(len(A[0])):
			if i not in V and A[index][i]+t<Narr[i] and A[index][i]!=-1:
				Narr[i]=A[index][i]
			elif i not in V and A[index][i]!=-1:
				Narr[i]=A[index][i]
	return sum
A=[[0,2,4,9,-1],[2,0,-1,-1,-1],[4,-1,0,3,-1],[9,-1,3,0,7],[-1,-1,-1,7,0]]
print(prim(A))