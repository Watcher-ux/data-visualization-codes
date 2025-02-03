#1 
def cross_product(a,b):
    import numpy as np
    c=np.cross(a,b)
    return c
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(cross_product(a,b))



#3
import numpy as np
import matplotlib.pyplot as plt

m = 20e-3  
k1 = 20  
k2 = 30  


omega1 = np.sqrt(k1 / m)
omega2 = np.sqrt(k2 / m)
t = np.linspace(0, 10, 1000)  
A1 = 1.0  
x1 = A1 * np.cos(omega1 * t)

A2=1.0
x2 = (A2 / 2) * np.cos(omega2 * t)


plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x1, label=f'k = {k1} N/m, A = {A1}')
plt.title('Motion of the Particle (Equilibrium Position)')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, x2, label=f'k = {k2} N/m, A = {A2/2}')
plt.title('Motion of the Particle (Halfway from Equilibrium Position)')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()

plt.tight_layout()
plt.show()

# Comparative Study
max_displacement_case1 = max(abs(x1))
max_displacement_case2 = max(abs(x2))
print(f"Maximum displacement in the first case: {max_displacement_case1} m")
print(f"Maximum displacement in the second case: {max_displacement_case2} m")

#another plot an interesting one
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np
labels=['ear','nose','throat']
abc=[23,45,56]
color=['green','blue','red']
plt.pie(abc,labels=labels,colors=color,autopct='%%3%f')
c=[2,3,4,6,8]
v=[7,9,0,4,3]
plt.scatter(c,v)
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('scatter plot')
plt.xticks(np.arange(min(c),max(v),1.0))
plt.axes(projection='3d')
plt.show()

























