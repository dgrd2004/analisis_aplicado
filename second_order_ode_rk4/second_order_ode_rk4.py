from math import exp

a = 0
b = 5
h = 0.01
x = 0
y = 2
yp = 3

def f(x, y, yp):
 return -4/3*yp + 1/3*(exp(-x) - 5)

def rk4_iter(f, h, x, y, yp):
 m, k = [0]*4, [0]*4
 m[0] = yp
 k[0] = f(x, y, yp)
 for i in list(range(3)):
  m[i+1] = yp + 1/2*h*k[i]
  k[i+1] = f(x + 1/2*h, y + 1/2*h*m[i], yp + 1/2*h*k[i])
 return y + h/6*(m[0] + 2*m[1] + 2*m[2] + m[3]), yp + h/6*(k[0] + 2*k[1] + 2*k[2] + k[3])

def rk4_second_order_solve(f, a, b, h, x, y, yp):
 total_pts = int((b-a)/h + 1)
 X, Y, YP = [0]*(total_pts - 1), [0]*(total_pts - 1), [0]*(total_pts - 1)
 X[0] = x
 Y[0] = y
 YP[0] = yp
 for i in list(range(total_pts - 2)):
  X[i + 1] = X[i] + h
  Y[i + 1], YP[i + 1] = rk4_iter(f, h, X[i], Y[i], YP[i])
 return X, Y, YP

x, y, yp = rk4_second_order_solve(f, a, b, h, x, y, yp)

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.grid(True)
plt.show()
