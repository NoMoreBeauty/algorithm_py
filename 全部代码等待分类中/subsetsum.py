def subsetsum(A,S,re,te,T):
	if A not in re and sum(A)==T:
		re.append(A[:])
	for i in range(te,len(S)):
		if sum(A)>T or sum(A)+sum(S)<T:
			break
		t,te=S[i],i
		A.append(t)
		subsetsum(A,S,re,te+1,T)
		A.remove(t)
re=[]
subsetsum([],[1,2,3,4],re,0,4)	
print(re)	