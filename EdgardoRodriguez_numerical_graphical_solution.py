import math
import numpy as N
import matplotlib.pyplot as plt
import pylab

def f(x):
 return math.sqrt(20**2 - x**2) - x*math.tan(x)

def my_bisect(eq, segment, ITER, TOL):
 a, b, i = segment['a'], segment['b'], 0
 FA, FB = eq(a), eq(b)
 if( FA*FB > 0 ):
  print('\nThere is no change of sign in this interval - BISECTION NOT POSSIBLE...')
 else :
  while True:
   i = i + 1
   p = a + (b - a)/2
   FP = eq(p)
   if FP == 0 or (b - a)/2 < TOL :
    print('\nProcedure completed successfully after', i, 'iterations.\nThe root found was x =', p, '\n')
    break
   else :
    if FA*FP > 0 :
     a = p
     FA = FP
    else :
     b = p
   if i == ITER :
    print('\nThe procedure was unsuccessful, after ', i, 'iterations convergence not reached.\nProgram execution stoped...\n')
    break

def numerical_solve():
 i = math.pi/2
 print('\nFor the open interval from' , 0, 'to', i, ':')
 my_bisect(f, {'a':0, 'b':i - 0.0001}, 20, 0.0001)
 while i < 20 :
  if i + math.pi <= 20 :
   print('\nFor the open interval from' , i, 'to', (i + math.pi), ':')
   my_bisect(f, {'a':i + 0.0001, 'b':i + math.pi - 0.0001}, 20, 0.0001)
  else :
   print('\nFor the open interval from' , i, 'to', 20, ':')
   my_bisect(f, {'a':i + 0.0001, 'b':20}, 20, 0.0001)
  i = i + math.pi

def graphical_solve():
 x = N.arange(0, 25, 0.01)
 plt.ylim(ymax = 25, ymin = 0)

 f = x*N.tan(x)
 g = ( (20)**2 - x**2 )**0.5
 
 pylab.plot(x , f , label = 'x*tan(x)')
 pylab.plot(x , g , label = '( (20)**2 - x**2 )**0.5')
 pylab.legend()
 pylab.show()

def main():
 numerical_solve()
 graphical_solve()

main()
