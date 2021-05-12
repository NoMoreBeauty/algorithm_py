input='carbohydrate'
#output = abort->5
A=list(input)
A.insert(0,'Z')
DP=[0 for _ in range(len(A))]
def selc(i):
	t=-1
	for j in range(i): 
		if A[j]<A[i] and DP[j]>t:
			t=DP[j]
	return t
for i in range(1,len(A)):
	DP[i]=selc(i)+1
print(max(DP))