def count_sort(A):
	count=[0 for i in range(max(A)+1)]
	B=A
	for i in A:
		count[i]+=1
	for j in range(1,len(count)):
		count[j]+=count[j-1]
	for k in A[::-1]:
		B[count[k]-1]=k
		count[k]-=1
	return B

A=[1,3,2,2,4,5,1,2,2,3]
B=count_sort(A)
print(B)
