import copy
class State:
	def __init__(self,S,upper=0,cost=0,n=0):
		self.upper=upper
		self.cost=cost
		self.volumn=S
		self.islive=1
		self.select=[-1 for i in range(n)]
	def set(self,V,W):
		index=0
		for i in range(len(self.select)):
			if self.select[i]==1:
				index=i
				self.cost+=V[i]
				self.volumn-=W[i]
				self.upper+=V[i]
		index+=1
		if self.volumn<0:
			self.islive=0
			self.upper=-1
			self.cost=-1
		while self.volumn>0 and index < len(W):
			if self.select[index]==0:
				index+=1
				continue
			if self.volumn>=W[index] :
				self.volumn-=W[index]
				self.cost+=V[index]
				self.upper+=V[index]
				index+=1
			else:
				self.upper+=self.volumn*V[index]//W[index]
				self.volumn=0
	def julive(self,bn):
		if self.upper<bn[0]:
			self.islive=0
		if self.cost>=bn[0]:
			bn[0]=self.cost
			bn[1]=self.select