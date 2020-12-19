# Paqueterías utilizadas
from numpy import *
import math
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

x = range(1,30,1)
y = np.round([1+1/n for n in range(1,30,1)], decimals = 5)
print(y)
plt.plot(x, y, 'o')
