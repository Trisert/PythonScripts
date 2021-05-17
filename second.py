import numpy as np

def calc(a,b,c):
    x1 = (-b + np.sqrt(b**2-4*a*c)) / 2*a
    x2 = (-b - np.sqrt(b**2-4*a*c)) / 2*a
    return x1,x2

a = int(input("Il primo termine: "))
b = int(input("Il secondo termine: "))
c = int(input("Il terzo termine: "))
print(calc(a, b, c))
