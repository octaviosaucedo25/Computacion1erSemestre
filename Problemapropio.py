from numpy import *
from scipy import *
import math
import numpy as np

r = float(input('Ingresa el valor de r, es decir, el módulo: '))
theta = float(input('Ingresa el valor del ángulo en grados sexagesimales: '))
theta2 = math.radians(t)
n = int(input('Ingresa la potencia n: '))
i = 0 + 1*j
zelevadoan = math.pow(r,n)*(np.round(math.cos(n*theta2), decimals = 5) + i*np.round(math.sin(n*theta2), decimals = 5))

print("El número complejo ingresado, elevado a la potencia",n,"es igual a",zelevadoan)
