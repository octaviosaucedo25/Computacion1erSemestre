from numpy import *
from scipy import *
import math
import numpy as np

r = float(input('Introduce el valor del módulo de z: '))
t = float(input('Introduce el valor del ángulo de z en grados: '))
t2 = math.radians(t)
n = int(input('¿A qué potencia será elevado z?: '))
z = (r,t)
i = 0 + 1j
potenciadez = math.pow(r,n)*(np.round(math.cos(n*t2), decimals = 4) + i*np.round(math.sin(n*t2), decimals = 4))

print("El número complejo",z,"elevado a la potencia",n,"es igual a",potenciadez)
