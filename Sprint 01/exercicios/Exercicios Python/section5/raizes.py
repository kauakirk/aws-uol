import sys
import os

def raizes(a, b, c):
    d = (b**2 - 4 *a*c)
    x1 = (-b + d**(1/2))/(2*a)
    x2 = (-b - d**(1/2))/(2*a)

    print(f"o valor de x1: {x1},  valor de x2: {x2}")
    
while True:
    try:
        a = float(input("entre com o valor de a: "))
        b = float(input("entre com o valor de b: "))
        c = float(input("entre com o valor de c: "))
    except ValueError:
        print("digite somente numeros")
    else:
        raizes(a, b, c)