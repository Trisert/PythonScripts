import sympy as sp
from sympy import solve 

x = sp.Symbol('x') 
y = sp.Symbol('y')  
print(solve(x**2-4*x-2,x))
