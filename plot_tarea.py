
#Edgardo Rodriguez

import numpy as N
import matplotlib.pyplot as plt

x = N.arange(0, 25, 0.01)
plt.ylim(ymax = 25, ymin = 0)

import pylab

f = x*N.tan(x)
g = ( (20)**2 - x**2 )**0.5

pylab.plot(x , f , label = 'x*tan(x)')
pylab.plot(x , g , label = '( (20)**2 - x**2 )**0.5')
pylab.legend()
pylab.show()
