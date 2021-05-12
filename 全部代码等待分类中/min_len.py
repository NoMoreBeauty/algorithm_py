import numpy as np
import math
def x_sort(B):
	A=B
	for i in range(len(A)):
		for j in range(len(A)-1):
			if A[j][0]>A[j+1][0]:
				A[j],A[j+1]=A[j+1],A[j]
	return A
def y_sort(B):
	A=B
	for i in range(len(A)):
		for j in range(len(A)-1):
			if A[j][1]>A[j+1][1]:
				A[j],A[j+1]=A[j+1],A[j]
	return A
def distance(A,B):
	return math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)

def Min_Len(A):
	n=len(A)
	if n==1:
		return 100
	if n==2:
		return distance(A[0],A[1])
	X_A=x_sort(A)
	mid=X_A[n//2][0]
	d1=Min_Len(X_A[:n//2])
	d2=Min_Len(X_A[n//2:])
	d=min(d1,d2)
	NEW=[]
	for i in X_A:
		if i[0]>=mid-d and i[0]<=mid+d:
			NEW.append(i)
	Y_A=y_sort(NEW)
	if len(Y_A)<=5:
		for j in range(len(Y_A)-1):
			for l in range(len(Y_A)-j-1):
				if distance(Y_A[j],Y_A[j+l+1])<d:
					d=distance(Y_A[j],Y_A[j+l+1])
	else:
		for j in range(len(Y_A)-5):
			for l in range(0,5):
				if distance(Y_A[j],Y_A[j+l])<d:
					d=distance(Y_A[j],Y_A[j+l])
	return d
A=[[1,2],[0,2],[1,0],[0,0],[0.5,0]]
print(Min_Len(A))