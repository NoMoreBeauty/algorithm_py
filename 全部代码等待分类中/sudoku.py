import copy
def isSafe(A):
	mode=[x for x in range(1,len(A)+1)]
	for i in range(1,len(A)+1):
		t=mode[:]
		for j in range(1,len(A)+1):
			if A[i-1][j-1] in t:
				t.remove(A[i-1][j-1])
			else:
				return False
	for i in range(1,len(A)+1):
		t=mode[:]
		for j in range(1,len(A)+1):
			if A[j-1][i-1] in t:
				t.remove(A[j-1][i-1])
			else:
				return False
	return True 
def find_emp(A):
	r=[]
	for i in range(len(A)):
		for j in range(len(A)):
			if A[i][j]==0:
				r.append([i,j])
	return r
def sudoku(A,re):
	emp_pos=find_emp(A)
	if isSafe(A) and A not in re and len(emp_pos)==0:
		re.append(copy.deepcopy(A))
	elif len(emp_pos)>0:
		for x in range(1,4):
			emp_pos=find_emp(A)
			i,j=emp_pos[0]
			A[i][j]=x
			sudoku(A,re)
			A[i][j]=0
re=[]
A=[[0,3,0],[0,0,1],[2,0,0]]
sudoku(A,re)
print(re)