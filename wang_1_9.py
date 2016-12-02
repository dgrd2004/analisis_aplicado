from sympy import *

x, y, z, xp, yp, zp, lin_charge_dens, permitivity, alpha, epsilon, l  = symbols('x y z xp yp zp lin_charge_dens permitivity alpha epsilon l')
A, a, b, c, L, = symbols('A a b c L', integer=True)
n = symbols( 'n', positive=True )

# PROBLEM 1.13

print('\n\n****Problem 1.13****\n\n')

V = Matrix([x*y, y*z, z*x]) # velocity vector definition

def partial_sumflux(i, j, j0, j1, k, k0, k1): # function of the partial sum of the flux in the direction of the i-th coordinate
 return integrate(V[i], (j, j0, j1), (k, k0, k1)) 

def eval_expr(expr, i, j, k): # evaluation of a function of x, y, z coordinates when x = i, y = j, z = k
 return expr.subs({x:i, y:j, z:k}).n()

def main_1_13():

 print('The velocity vector is:')
 pprint(V)

 px = partial_sumflux(0, y, 0, b, z, 0, c)
 py = partial_sumflux(1, z, 0, c, x, 0, a)
 pz = partial_sumflux(2, x, 0, a, y, 0, b)
 
 px_evaluated = -1*eval_expr(px, 0, 0, 0) + eval_expr(px, a, 0, 0)
 py_evaluated = -1*eval_expr(py, 0, 0, 0) + eval_expr(py, 0, b, 0)
 pz_evaluated = -1*eval_expr(pz, 0, 0, 0) + eval_expr(pz, 0, 0, c)

 print('\nThe flux contribution in the x direction is:\n')
 pprint(px_evaluated)
 print('\nThe flux contribution in the y direction is:\n')
 pprint(py_evaluated)
 print('\nThe flux contribution in the z direction is:\n')
 pprint(pz_evaluated)

 print('\nThe total flux through the closed surface is;\n')
 pprint(px_evaluated + py_evaluated + pz_evaluated)

main_1_13() # end of problem 1.13

print('\n\n') 

# PROBLEM 2.9

print('****Problem 2.9****')

r = Matrix([a, y])
rp = Matrix([0, yp])
R = rp - r

def electric_force_component(i):
 return integrate(-1*(lin_charge_dens**2*R[i])/(4*pi*sqrt(R.dot(R))**(3)), (yp, 0, L), (y, 0, L))

def main_2_9():
 print( '\nSolving the resulting vector argument integral ("x" "y" components respectively):\n\n',pretty( Integral(-1*(lin_charge_dens**2*R)/(4*pi*permitivity*sqrt(R.dot(R))**(3)), (yp, 0, L), (y, 0, L)) ) )
#print('The force component in the x direction is:\n\n', pretty(electric_force_component(0)))
#print('The force component in the y direction is:\n', electric_force_component(1)) #****ERROR SOLVING THE SECOND INTEGRAL****
 
main_2_9()

print('\n\n')

# PROBLEM 3.10

print('****Problem 3.10****\n\n')

r = Matrix([0, 0, z])
rp = Matrix([a*cos(y), a*sin(y), 0])
R = rp - r

def main_3_10():
 print( 'Using the cylindrical coordinate system with x = rho, y = phi, z = z\n' )
 print( 'Solving the integral for the electric field:\n', pretty(Integral((-1*lin_charge_dens*a*R)/(4*pi*epsilon*sqrt(trigsimp(R.dot(R)))**3), (y, -alpha, alpha))))
 print('\nWere the vector R is:\n')
 pprint(R)
 print( '\nThe evaluation results:\n' )
 result = Integral((-1*lin_charge_dens*a*R)/(4*pi*epsilon*sqrt(trigsimp(R.dot(R)))**3), (y, -alpha, alpha)).doit()
 pprint( result )
 print( '\nWhen alpha = pi then:\n' )
 pprint( result.subs( alpha, pi ) )

main_3_10()

print( '\n\n' )

# PROBLEM 5.9

print( '****Problem 5.9****\n\n' )

potential = Integral( (A*x**(n + 2))/(4*pi*epsilon*sqrt( x**2 + l**2 - 2*x*l*z )), (x, 0, a), (y, 0, 2*pi), (z, -1, 1)  )
print( 'Solving the integral for the potential field:\n', pretty( potential ) )
print( type( n ) )
pprint( potential.doit() )
