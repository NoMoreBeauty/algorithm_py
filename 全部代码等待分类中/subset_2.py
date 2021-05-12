re=[]
S=[1,2,3]
def subset(A,te):
	if A not in re:
		re.append(A[:])
	for i in range(te,len(S)):
		A.append(S[i])
		subset(A,i+1)
		A.pop(-1)
subset([],0)	
print(re)