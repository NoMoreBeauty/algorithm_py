#Strassen 算法 时间复杂度O(n^log7)
def Matrix_Add(A,B):
	n=len(A)
	C=[[0 for i in range(n)] for j in range(n)]
	if n==1:
		C[0][0]=A[0][0]+B[0][0]
		return C
	for i in range(n):
		for j in range(n):
			C[i][j]=A[i][j]+B[i][j]
	return C
def Matrix_Sub(A,B):
	n=len(A)
	C=[[0 for i in range(n)] for j in range(n)]
	if n==1:
		C[0][0]=A[0][0]-B[0][0]
		return C
	for i in range(n):
		for j in range(n):
			C[i][j]=A[i][j]-B[i][j]
	return C
def patition(A):
	n=len(A)
	A1=[[0 for i in range(n//2)] for j in range(n//2)]
	A2=[[0 for i in range(n//2)] for j in range(n//2)]
	A3=[[0 for i in range(n//2)] for j in range(n//2)]
	A4=[[0 for i in range(n//2)] for j in range(n//2)]
	for i in range(n):
		for j in range(n):
			if i<n//2 and j<n//2:
				A1[i][j]=A[i][j]
			elif i<n//2 and j>=n//2:
				A2[i][j-n//2]=A[i][j]
			elif i>=n//2 and j<n//2:
				A3[i-n//2][j]=A[i][j]
			else :
				A4[i-n//2][j-n//2]=A[i][j]
	return A1,A2,A3,A4
def mesh(C11,C12,C21,C22):
	n=2*len(C11)
	C=[[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			if i<n//2 and j<n//2:
				C[i][j]=C11[i][j]
			elif i<n//2 and j>=n//2:
				C[i][j]=C12[i][j-n//2]
			elif i>=n//2 and j<n//2:
				C[i][j]=C21[i-n//2][j]
			else :
				C[i][j]=C22[i-n//2][j-n//2]
	return C
def Matrix_Mul(A,B):
	n=len(A)
	C=[[0 for i in range(n)] for j in range(n)]
	if n==1:
		C[0][0]=A[0][0]*B[0][0]
		return C
	A11,A12,A21,A22=patition(A)
	B11,B12,B21,B22=patition(B)
	M1=Matrix_Mul(A11,Matrix_Sub(B12,B22))
	M2=Matrix_Mul(Matrix_Add(A11,A12),B22)
	M3=Matrix_Mul(Matrix_Add(A21,A22),B11)
	M4=Matrix_Mul(A22,Matrix_Sub(B21,B11))
	M5=Matrix_Mul(Matrix_Add(A11,A22),Matrix_Add(B11,B22))
	M6=Matrix_Mul(Matrix_Sub(A12,A22),Matrix_Add(B21,B22))
	M7=Matrix_Mul(Matrix_Sub(A11,A21),Matrix_Add(B11,B12))
	C11=Matrix_Add(Matrix_Sub(Matrix_Add(M5,M4),M2),M6)
	C12=Matrix_Add(M1,M2)
	C21=Matrix_Add(M3,M4)
	C22=Matrix_Sub(Matrix_Sub(Matrix_Add(M5,M1),M3),M7)
	C=mesh(C11,C12,C21,C22)
	return C
A=[[2,2,3,5],[1,8,2,2],[2,2,3,5],[1,8,2,2]]
B=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
C=Matrix_Mul(A,B)
print(C)
