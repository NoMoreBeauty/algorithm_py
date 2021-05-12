def find_longest(A):
	sub=[0 for i in range(max(A)+2)]
	for i in A:
		sub[i]=sub[i-1]+sub[i+1]+1
		m,n=i-1,i+1
		while sub[m]!=0 and m>=0:
			sub[m]=sub[i]
			m-=1
		while sub[n]!=0 and n>=0:
			sub[n]=sub[i]
			n+=1
	return max(sub)
A=[12,1,3,4,2,9,8]
print(find_longest(A))