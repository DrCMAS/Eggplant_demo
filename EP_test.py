import numpy as np
import matplotlib.pylab as plt

x=np.random.randint(0,100,20)
y=np.random.randint(0,100,20)

m,c=np.polyfit(x,y,1)

plt.plot(x,y,'x')
plt.plot(x,(m*x+c))

plt.savefig('Test.png')