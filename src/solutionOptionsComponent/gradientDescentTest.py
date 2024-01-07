from sympy import *
from sympy import Array

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u ,v ,w, x, y, z = symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")

f = sympify("x**2+y**2")

set_of_symbols = f.free_symbols
list_of_symbols = list(set_of_symbols)

array =[]
for i in range(len(list_of_symbols)):
  array.append(f.diff(list_of_symbols[i]))
  
gradient = Array(array)


def gradient_descent(vect, num_steps, step_size):
  for i in range(num_steps):
    vect = vect - step_size * gradient.subs(x,vect[0]).subs(y,vect[1])
  return vect

vector = Array([1,2])
print(gradient_descent(vector, 100, 0.1))
