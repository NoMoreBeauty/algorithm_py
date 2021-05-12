#divided and conquer
inputy=[-1,1,1,1,9,9,8,2,3,-4,2]
def dc(A):
	if len(A)==2:
		return max(0,A[0],A[1],A[0]*A[1])
	if len(A)==1:
		return max(0,A[0])
	mid=len(A)//2
	if len(A)>=5:
		x=A[mid]*A[mid+1]+dc(A[:mid])+dc(A[mid+2:])
		y=dc(A[:mid+1])+dc(A[mid+1:])
		return max(x,y)
	else:
		x=A[mid]*A[mid+1]+dc(A[:mid])
		y=dc(A[:mid+1])+dc(A[mid+1:])
		return max(x,y)
print(f"分治法的结果：{dc(inputy)}")
#dp
l=len(inputy)
DP=[0 for _ in range(len(inputy)+2)]
inputy.append(1)
for i in range(l-1,-1,-1):
	DP[i]=max(DP[i+1],inputy[i]+DP[i+1],inputy[i]*inputy[i+1]+DP[i+2])
print(f"动态规划的结果：{DP[0]}")