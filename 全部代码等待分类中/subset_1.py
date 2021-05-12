def subset(A,S,re):
	if len(A)==len(S):
		re.append(A[:])
	for i in range(2):
		A.append(i)
		if len(A)<=len(S) and A not in re:
			subset(A,S,re)
		A.pop(-1)
def showInfo(re,S):
	r=[[] for x in range(len(re))]
	for i in range(len(re)):
		for j in range(len(re[i])):
			if re[i][j]==1:
				r[i].append(S[j])
	return r
re=[]
subset([],[1,2,3],re)
r=showInfo(re,[1,2,3])
print(r)

