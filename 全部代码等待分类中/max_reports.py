def sec(E):
	return E[1]
def max_reports(A):
	A.sort(key=sec)
	sum=0
	t=0
	for i in A:
		if i[0]>=t:
			sum+=1 
			t=i[1]
	return sum
print(f"最多听 {max_reports([[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]])} 场学术报告")