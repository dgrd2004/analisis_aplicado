from math import sqrt
import numpy as N
import pylab as plt

#PARAMETER DEFINITION
a = 0
b = 2
h = 0.01
t = 0
x = 0
y = 0
velocity = 20
alpha = N.pi/4
beta = N.pi/8
#*******************

def f(t, x, y, xp, yp):
 k = 0.1
 m = 1
 g = 9.81
 return -k/m*xp*sqrt(xp**2 + yp**2)

def g(t, x, y, xp, yp):
 k = 0.1
 m = 1
 g = 9.81
 return -g - k/m*yp*sqrt(xp**2 + yp**2)

def rk4_2nd_order_iter(f, g, h, t, x, y, xp, yp):
 K0x = f(t,x,y,xp,yp)            
 K0y = g(t,x,y,xp,yp)
 Q1x = xp + (h/2)*K0x            
 Q1y = yp + (h/2)*K0y
 K1x = f(t+h/2,x+(h/2)*xp,y+(h/2)*yp,Q1x,Q1y)    
 K1y = g(t+h/2,x+(h/2)*xp,y+(h/2)*yp,Q1x,Q1y)
 Q2x = xp + (h/2)*K1x           
 Q2y = yp + (h/2)*K1y
 K2x = f(t+h/2,x+(h/2)*Q1x,y+(h/2)*Q1y,Q2x,Q2y)   
 K2y = g(t+h/2,x+(h/2)*Q1x,y+(h/2)*Q1y,Q2x,Q2y)
 Q3x = xp + h*K2x         
 Q3y = yp + h*K2y
 K3x = f(t+h, x+h*Q2x, y+h*Q2y, Q3x,Q3y)      
 K3y = g(t+h, x+h*Q2x, y+h*Q2y, Q3x,Q3y)
 return x + h*(xp+(h/6)*(K0x + K1x + K2x)), y + h*(yp+(h/6)*(K0y + K1y + K2y)), xp + (h/6)*(K0x + 2*K1x + 2*K2x + K3x), yp + (h/6)*(K0y + 2*K1y + 2*K2y + K3y)

def rk4_coupled_second_order_solve(f, g, a, b, h, t, x, y, xp, yp):
 total_pts = int(round(((b-a)/h), 0))
 print('Total points: ', total_pts)
 T, X, Y, XP, YP = [0]*total_pts, [0]*total_pts, [0]*total_pts, [0]*total_pts, [0]*total_pts
 T[0] = t
 X[0] = x
 Y[0] = y
 XP[0] = xp
 YP[0] = yp
 for i in list(range(total_pts - 1)):
  T[i + 1] = T[i] + h
  X[i + 1], Y[i + 1], XP[i + 1], YP[i + 1] = rk4_2nd_order_iter(f, g, h, T[i], X[i], Y[i], XP[i], YP[i])
  print('performing iteration ', i + 1)
 return T, X, Y, XP, YP

T, X, Y, XP, YP = rk4_coupled_second_order_solve(f, g, a, b, h, t, x, y, velocity*N.cos(alpha + beta), velocity*N.sin(alpha + beta))

l_x = N.arange(0, 10, h)
l_y = N.tan(alpha)*l_x
plt.plot(X, Y)
plt.plot(l_x, l_y)
print('Generating graph...')
plt.grid(True)
print('Now presenting graph on screen...')
plt.show()
print('Program succesfully executed.')
