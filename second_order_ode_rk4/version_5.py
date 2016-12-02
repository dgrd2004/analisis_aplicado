from math import exp

def f(x, y, u):
 return -4/3*u + 1/3*(exp(-x) - 5)

def rk4_iter(f, h, x, y, u):
 m, k = [0]*4, [0]*4
 m[0] = u
 k[0] = f(x, y, u)
 for i in list(range(3)):
  m[i+1] = u + 1/2*h*k[i]
  k[i+1] = f(x + 1/2*h, y + 1/2*h*m[i], u + 1/2*h*k[i])
 return y + h/6*(m[0] + 2*m[1] + 2*m[2] + m[3]), u + h/6*(k[0] + 2*k[1] + 2*k[2] + k[3])

def rk4_second_order_solve(f, a, b, h, x, y, u):
 total_pts = int((b-a)/h + 1)
 X, Y, U = [0]*(total_pts - 1), [0]*(total_pts - 1), [0]*(total_pts - 1)
 X[0] = x
 Y[0] = y
 U[0] = u
 for i in list(range(total_pts - 2)):
  X[i + 1] = X[i] + h
  Y[i + 1], U[i + 1] = rk4_iter(f, h, X[i], Y[i], U[i])
 return X, Y, U

x, y, u = rk4_second_order_solve(f, 0, 5, 0.01, 0, 2, 3)

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.grid(True)
plt.show()
