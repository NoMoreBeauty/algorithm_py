class Dsu:
	def __init__(self,n):
		self.n=[i for i in range(n)]
		self.fa=self.n
		self.rank=[1 for x in range(n)]
	def find_fa(self,tar):
		if tar==self.fa[tar]:
			return tar
		else:
			self.fa[tar]=self.find_fa(self.fa[tar])
			return self.fa[tar]
	def union_find(self,x,y):
		m=self.find_fa(x)
		n=self.find_fa(y)
		if m==n:
			return False
		if self.rank[m]>=self.rank[n]:
			self.fa[n]=m
		else:
			self.fa[m]=n
		if self.rank[m]==self.rank[n] and m!=n:
			self.rank[m]+=1
		return True
	def print(self):
		print(f"父节点：{self.fa}")
		print(f"深度：{self.rank}")
if __name__=='__main__':
	x=Dsu(5)
	x.union_find(0,1)
	x.union_find(2,3)
	x.union_find(0,2)
	x.union_find(4,3)
	x.union_find(0,4)
	x.print()



