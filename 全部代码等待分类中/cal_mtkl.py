import matplotlib.pyplot as plt
import numpy as np
from random import random
import math
SIZE=100000
X1,X2,Y1,Y2,=[],[],[],[]

x=np.linspace(0,np.pi,256,endpoint=80) #图像横坐标范围
y=np.sin(x)
for i in range(SIZE):
    a,b = random()*np.pi,random()
    if b<math.sin(a):
    	X1.append(a)
    	Y1.append(b)
    else:
    	X2.append(a)
    	Y2.append(b)
fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(X1,Y1,s=len(X1)/1000000,color='green')
ax.scatter(X2,Y2,s=len(X2)/1000000,color='blue')
plt.plot(x,y,color='red',linewidth=2,linestyle='-') #根据x y 数组绘制直线曲线
plt.show()
