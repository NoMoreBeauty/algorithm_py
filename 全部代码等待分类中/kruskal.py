from dsu import Dsu
def Kruskal(A):
	dsu=Dsu(len(A[0]))
	S=[]
	sum=0
	while len(S)<5:
		t=100
		i1=0
		j1=0
		for i in range(1,len(A[0])):
			for j in range(i):
				if A[i][j]!=-1 and A[i][j]<t:
					i1,j1,t=i,j,A[i][j]
		A[i1][j1]=-1   #找过的边清除掉
		ju=dsu.union_find(i1,j1) #用并查集判断是否成环
		if ju:  #如果ju返回true则表明执行了合并操作，没有成环
			if i1 not in S:
				S.append(i1)
			if j1 not in S:
				S.append(j1)
			sum+=t #总路径
	return sum
A=[[0,2,4,9,-1],[2,0,-1,-1,-1],[4,-1,0,3,-1],[9,-1,3,0,7],[-1,-1,-1,7,0]]
x=Kruskal(A)
print(f"MST的权重和为：{x}")