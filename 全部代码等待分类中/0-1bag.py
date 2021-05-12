import copy
from state import State
def bag(W,V,M):
	Z=list(zip(W,V))
	Z.sort(key=lambda x:x[1]//x[0],reverse=True)
	w,v=zip(*Z)
	S=[]
	s0=State(M,n=len(W))
	for i in range(len(w)):
		if s0.volumn-w[i]>0:
			s0.cost+v[i]
	bn=[s0.cost,[]]
	y=0
	while y <len(W):
		lg=len(S)
		s1=State(M,n=len(W))
		s2=State(M,n=len(W))
		if lg!=0:
			s=S[0]
			s1.select=copy.deepcopy(s.select)
			s2.select=copy.deepcopy(s.select)
			S.remove(s)
		s1.select[y]=1
		s2.select[y]=0
		s1.set(V,W)
		s2.set(V,W)
		s1.julive(bn)
		s2.julive(bn)
		t1=copy.deepcopy(s1)
		t2=copy.deepcopy(s2)
		S.append(t1)
		S.append(t2)
		jon=[]
		for i in range(len(S)):
			if S[i].islive==1:
				jon.append(S[i])
		if t1 not in jon and t2 not in jon:
			y-=1
		S=copy.deepcopy(jon)
		S.sort(key=lambda s:s.upper,reverse=True)
		y+=1
	print(bn[1])
bag([2,4,6,9],[10,10,12,18],15)