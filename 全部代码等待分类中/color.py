import copy
def isSafe(S,A):
	for x,y in S.items():
		for i in y:
			if A[x]==A[i] or A[x]==-1 or A[i]==-1:
				return False
	return True
def count_color(A):
	s=[]
	for i in A.values():
		if i not in s:
			s.append(i)
	return len(s)
def find_noclo(A):
	r=[]
	for x,y in A.items():
		if y==-1:
			r.append(x)
	return r 
def color(S,A,re):
	emp=find_noclo(A)
	if isSafe(S,A) and A not in re and re[0]>=count_color(A):
		re[0]=count_color(A)
		re.append(copy.deepcopy(A))
	elif len(emp)>0:
		for i in range(4):
			A[emp[0]]=i
			color(S,A,re)
			A[emp[0]]=-1

S={'A':['B','C','D'],'B':['A','D'],'C':['A','D'],'D':['A','C']}
#Ans={'A':0,'B':1,'C':1,'D':2}
Ans={'A':-1,'B':-1,'C':-1,'D':-1}
re=[100]
color(S,Ans,re)
print(re[1:])