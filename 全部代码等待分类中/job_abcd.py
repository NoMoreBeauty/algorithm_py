import copy
import sys
class Job:
	def __init__(self):
		self.upper=0
		self.road=[]
def cal(A,x):
	sum=0
	for i in range(len(x)):
		sum+=A[i][x[i]]
	for j in range(len(x),len(A)):
		t=sys.maxsize
		for l in range(len(A)):
			if l not in x and A[j][l]<t:
				t=A[j][l]
		sum+=t
	return sum
def min_job_cost(A):
	S=[]
	for i in range(len(A)):
		j=Job()
		j.road.append(i)
		j.upper=cal(copy.deepcopy(A),j.road)
		S.append(copy.deepcopy(j))
	while  len(S[0].road)!=4 :
		s=S[0]
		for i in range(len(A)):
			if i not in s.road:
				j=Job()
				j.road=copy.deepcopy(s.road)
				j.road.append(i)
				j.upper=cal(copy.deepcopy(A),j.road)
				S.append(copy.deepcopy(j))
		S.remove(s)
		S.sort(key=lambda s:s.upper)
	print(S[0].road)
A=[[9,2,7,8],[6,4,3,7],[5,8,6,8],[7,6,9,4]]
min_job_cost(A)