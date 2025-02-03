import numpy
a=numpy.array([1,2,3])
b=numpy.array([2,3,4])
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.divide(a,b))
print(numpy.dot(a,b))

#from stackoverflow
def dot(s,d):
    return sum(x*y for x,y in zip(s,d))
s=[1,3,5]
d=[4,6,7]
print(dot(s,d))

import matplotlib.pyplot as plt
x=[-1,0,1,2,3,4]
y=[-1,0,1,2,2,3]
x2=[1,2,3,4]
y2=[4,3,2,1]
plt.plot(x2,y2,color='black',linestyle='solid',linewidth='4',marker='p',markerfacecolor='blue',markersize='14',label='line1')
plt.plot(x,y,color='black',linestyle='solid',linewidth='4',marker='v',markerfacecolor='red',markersize='14',label='line2')
plt.xlabel('x-axis',fontsize='16')
plt.ylabel('y-axis',fontsize='16')
plt.title('two lines on same graph',fontsize='16')
plt.legend()
plt.autumn()
plt.axhspan(ymin=2.3,ymax=3.5)
plt.show()
plt.axhline(xmin=2.6,xmax=5)


import numpy as np
list1=[1,2,3,4]
list2=[5,6,7,8]
vector1=np.array(list1)
print("The first vector is:",str(vector1))
vector2=np.array(list2)
print("The SECOND vector is:",str(vector2))
sum_vector=vector1+vector2
print(sum_vector)
sub_vector=vector2-vector1
print(sub_vector)

#to make column vectors

v=[[3],[4],[5],[6]]
vectorv=np.array(v)
print(vectorv)



























