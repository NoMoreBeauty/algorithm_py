def ar_test(A):
	leng=len(A)
	if leng==1:
		return True
	for i in range(leng-1):
		if (A[-1]-A[i])/(leng-1-i)==1 or (A[-1]-A[i])/(leng-1-i)==-1:
			return False
	return True
def back_track(A,L,re,n):
	if len(A)==n and A not in re:
		re.append(A[:])
	else:
		for i in range(len(L)):
			t=L[i]
			A.append(t)
			L.remove(t)
			if ar_test(A):
				back_track(A,L,re,n)
			A.remove(t)
			L.insert(i,t)
		return False
def n_queen(n):
	re=[]
	N=[]
	L=[x for x in range(n)]
	back_track(N,L[:],re,n)	
	#print(re)
	print(f"有{len(re)}个解")
n_queen(8)