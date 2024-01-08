from sympy import *
from sympy import Array
import math

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u ,v ,w, x, y, z = symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")

func= a*x**2 + b*y**2
ar = [[1,1,2],[2,2,8]]
params = [a,b]
vars = [x,y]
s = 0


for i in range(len(ar)):
  newFunc = func
  term1 = ar[i][-1]
  for j in range(len(vars)):
    newFunc = newFunc.subs(vars[j], ar[i][j])
  term2 = newFunc
  term = (term1 - term2)**2
  s = s + term
f = s 

set_of_symbols = f.free_symbols
list_of_symbols = list(set_of_symbols)
params = list_of_symbols


array =[]
for i in range(len(list_of_symbols)):
  array.append(f.diff(list_of_symbols[i]))


gradient = Array(array)

def gradient_descent(vect, num_steps, step_size):
  for i in range(num_steps):
    newGradient = gradient
    for j in range(len(params)):
      newGradient = newGradient.subs(params[j], vect[j])
    #if (i == 1):
      #print(newGradient)
    vect = vect - step_size * newGradient
  return vect

vector = []
for i in range(len(params)):
  vector.append(3)
  
vector = Array(vector)

print(gradient_descent(vector, 1000, 0.0001))
