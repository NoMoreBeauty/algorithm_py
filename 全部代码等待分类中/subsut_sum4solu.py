import sys
A=[-9,1,-5,4,3,-6,7,8,-2]
def solu1(A):#暴力循环O(n^3)
	s=0
	for i in range(len(A)):
		for j in range(i+1,len(A)+1):
			t=sum(A[i:j])#求sum的过程其实是一次循环
			if t>s:
				s=t
	return s
def solu2(A):#xyd.py前后扫描
	index_begin=0
	index_end=len(A)-1
	t,temp=0,0
	for i in range(len(A)):
		t+=A[i]
		if t>temp:
			temp=t
			index_begin=i
	t,temp=0,0
	for i in range(len(A)-1,-1,-1):
		t+=A[i]
		if t>temp:
			temp=t
			index_end=i
	return sum(A[index_end:index_begin+1])
def solu3(A):#分治法
	if len(A)<=1:
		return A[0]
	mid=len(A)//2
	L=solu3(A[:mid])
	R=solu3(A[mid:])
	lr,ll,t=0,0,0
	for i in A[mid:]:
		t+=i
		if t>lr:
			lr=t
	t=0
	for i in reversed(A[:mid]):
		t+=i
		if t>ll:
			ll=t
	l=ll+lr	
	return max(L,R,l)
def solu4(A):#动态规划
	r=[-sys.maxsize for _ in range(len(A))]
	r[0]=A[0]
	#定义r[i]为下标范围在0到i中的子序列，以第i位就是A[i]结尾的子序列中的最大子序列和
	for i in range(1,len(A)):
		r[i]=max(r[i-1]+A[i],A[i])
	return max(r)
print(solu1(A))
print(solu2(A))
print(solu3(A))
print(solu4(A))