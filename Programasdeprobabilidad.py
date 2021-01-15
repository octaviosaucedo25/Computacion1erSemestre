                                  # PAQUETERÍAS

import math
import numpy as np
import random as rnd
import matplotlib.pyplot as plt

                                  # PROBLEMA 1

print("PROBLEMA 1: Escribe un programa que realice una grafica del valor al que converge la probabilidad de tirar una moneda N veces (hay un resultado para Águila y uno para Sol).")  
                                
Ns = []    # Aquí guardamos el número de experimentos
ProbA = [] # Aquí se guardan los valores de la probabilidad de sacar águila. 
ProbS = [] # Aquí se guardan los valores de la probabilidad de sacar sol.  

for N in range(1,501):  # Definimos el número de experimentos N. Es el CICLO FOR principal.
    
    # La cantidad de veces que salió águila y sol comienzan en 0.
    aguilas = 0 
    soles = 0
    # La probabilidad de obtener cada lado de la moneda comienza en 0 (Opcional).
    pA = 0
    pS = 0
    
    for i in range(N):
        lanzamiento = rnd.random()  # Definimos el lanzamiento de la moneda con rnd.random.
        if lanzamiento > 0.5:       # Si el número es mayor a 0.5, sumar 1 a "aguilas".
            aguilas += 1                                                                  
        else:                       # En caso contrario, sumar 1 a "soles".
            soles += 1
        # Es decir, se acumula el número de veces que cayó cada lado de la moneda.
 
    pA = float(aguilas)/float(N) # Probabilidad de obtener águila.
    pS = float(soles)/float(N)   # Probabilidad de obtener sol.
     
    Ns.append(N)      # Agregamos cada valor de N en la lista con el mismo nombre.
    ProbA.append(pA)  # Agregamos los valores de pA para cada valor de N en la lista ProbA.
    ProbS.append(pS)  # Agregamos los valores de pS para cada valor de N en la lista ProbS.

plt.plot(Ns,ProbA,'.',color='brown')    # Gráfica de ProbA VS N.
plt.plot(Ns,ProbS,'.',color='gold')     # Gráfica de ProbS VS N.
plt.axhline(0.5,color='black')          # Línea horizontal en P(A,B)=0.5, el cual es el valor al que convergen las probabilidades.
plt.title("Gráfica de $P(A,S)$ vs $N$") # Título de la gráfica. Donde P(A,B) significa "Probabilidad de obtener Águila y Sol"
plt.xlabel("$N$")                       # Título del eje X "Número de experimentos o lanzamientos".
plt.ylabel("$P(A,B)$")                  # Título del eje Y "Probabilidad de obtener Águila y Sol"

plt.show()
                                   # PROBLEMA 2

print("PROBLEMA 2: Escribe un programa que realice una gráfica del valor al que converge la probabilidad de sacar un 3 al tirar un dado de 6 caras N veces.")
                                   
Ns_1 = []     # Aquí guardamos el número de experimentos
Prob3 = []  # Aquí se guardan los valores de la probabilidad de obtener un 3 al tirar un dado. 

for n in range(1,701):  # Definimos el número de experimentos n. Es el CICLO FOR principal.
    
    # La cantidad de veces que salió un 3 comienza en 0. 
    sacar3 = 0
    # Los valores de la probabilidad de sacar un 3 comienzan en 0 (Opcional).
    #p3 = 0
    
    for i in range(n):
        lanzamiento = rnd.randint(1,6)  # Se lanza el dado con rnd.randint(a,b) para que devuelva un número entero aleatorio entre 1 y 6.
        if lanzamiento == 3:            # Si el número obtenido es el 3, entonces sumar 1 a "sacar3".
            sacar3 += 1
    
    # La probabilidad de sacar un 3 se calcula dividiendo el número de veces que salió un 3 entre el número de experimentos.
    p3 = float(sacar3)/float(n)  
    
    Ns_1.append(n)      # Agregamos cada valor de N en la lista con el mismo nombre.
    Prob3.append(p3)  # Agregamos los valores de p3 para cada valor de N en la lista Prob3.
    
plt.plot(Ns_1,Prob3,'.',color='navy')      # Gráfica de Prob3 VS n.
plt.axhline(1/6,color='orangered')       # Línea horizontal en P(3)=1/6, el cual es el valor al que converge la probabilidad.
plt.title("Gráfica de $P(3)$ vs $n$")    # Título de la gráfica. Donde P(3) significa "Probabilidad de obtener un 3 al tirar un dado"
plt.xlabel("$n$")                        # Título del eje X "Número de experimentos o lanzamientos".
plt.ylabel("$P(3)$")                     # Título del eje Y "Probabilidad de obtener un 3"

plt.show()
                                     # PROBLEMA 3
    
print("PROBLEMA 3: Escribe un programa que realice una gráfica del valor al que converge la probabilidad de tirar 2 dados de 6 caras N veces y que la suma de los valores sea igual a 8, así como la de no obtenerlo.")
                                     
Ns_2 = []           # Aquí guardamos el número de experimentos
ProbSuma8 = []    # Aquí se guardan los valores de la probabilidad de obtener un 8 mediante la suma de dos dados.
ProbNoSuma8 = []  # Aquí se guardan los valores de la probabilidad de no obtener un 8 mediante la suma de dos dados.

for N_1 in range(1,801):  # Definimos el número de experimentos N. Es el CICLO FOR principal.
    
    # La cantidad de veces que la suma fue 8 comienza en 0, así como la de no obtenerla.
    sacarSuma8 = 0
    sacarNoSuma8 = 0
    # Los valores de la probabilidad de que la suma sea 8 comienza en 0 (Opcional).
    #pSuma8 = 0
    # Los valores de la probabilidad de que la suma no sea 8 comienza en 0 (Opcional).
    #pSumaNo8 = 0
    
    for i in range(N_1):
        dado_1 = rnd.randint(1,6)  # Se lanzan dos dados con rnd.randint(a,b) para que devuelva un número entero aleatorio entre 1 y 6.
        dado_2 = rnd.randint(1,6)
        if dado_1 + dado_2 == 8:   # Si la suma da 8, sumar 1 a "sacarSuma8".       
            sacarSuma8 += 1     
        else:                      # En cualquier otro caso, sumar 1 a "sacarNoSuma8".
            sacarNoSuma8 += 1
    
    # Definición de las probabilidades (eventos favorables/total de eventos).
    pSuma8 = float(sacarSuma8)/float(N_1)
    pNoSuma8 = float(sacarNoSuma8)/float(N_1)
    
    # Agregamos los valores de "N" y las dos probabilidades en sus respectivas listas.
    Ns_2.append(N_1)
    ProbSuma8.append(pSuma8)
    ProbNoSuma8.append(pNoSuma8)
    
plt.plot(Ns_2,ProbSuma8,'.',color='navy')         # Gráfica de P(Suma8) VS N.  
plt.plot(Ns_2,ProbNoSuma8,'.',color='orangered')  # Gráfica de P(NoSuma8) VS N.
plt.axhline(5/36,color='orangered')             # Línea horizontal en P(Suma8)=5/36, el cual es el valor al que converge la probabilidad.
plt.axhline(31/36,color='blue')                 # Línea horizontal en P(NoSuma8)=31/36, el cual es el valor al que converge la probabilidad.              
plt.title("Gráfica de $P(Suma)$ vs $N$")        # Título de la gráfica.
plt.xlabel("$N$")                               # Título del eje X "Número de eventos".
plt.ylabel("$Probabilidad$")                    # Título del eje Y "Probabilidades"

plt.show()

print("A continuación se muestran las dos gráficas anterior por separado:")

print("Probabilidad de que la suma de ambos dados sea igual a 8.")
plt.plot(Ns_2,ProbSuma8,'.',color='green')   
plt.axhline(5/36,color='red')   
plt.title("$P(d_{1}+d_{2}=8)$ vs $N$")       
plt.xlabel("$N$")                              
plt.ylabel("$Probabilidad$") 
plt.show()

print("Probabilidad de que la suma de ambos dados sea diferente de 8.")
plt.plot(Ns_2,ProbNoSuma8,'.',color='navy')
plt.axhline(31/36,color='orangered')  
plt.title("$P( d_{1}+d_{2} \in [2,7] \cup [9,12] )$ vs $N$")       
plt.xlabel("$N$")                              
plt.ylabel("$Probabilidad$")    
plt.show()
