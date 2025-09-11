#%%
from mis_funciones import gpa_enteros

def dados(N,x0=252):
    
    nros=[]
    numero=0
    m=2**32	
    a=1664525
    c=1013904223
    _nros= gpa_enteros(N,x0,a,c,m)
    for i in range(N):
        numero = 1 + int((_nros[i] / m) * (6 - 1 + 1))
        nros.append(numero)
    return nros


    

def dado_doble(N,x0=252):

    nros=[]
    numero=0
    m=2**32	
    a=1664525
    c=1013904223
    _nros= gpa_enteros(N,x0,a,c,m)
    for i in range(N):
        numero = 2 + int((_nros[i] / m) * (12 - 2 + 1))
        nros.append(numero)
    return nros


import numpy as np #pyright: ignore[reportMissingImports]
import matplotlib.pyplot as plt #pyright: ignore[reportMissingModuleSource]

# Distribucion teorica
var_al=np.arange(2,13)
dist_probabilidad=[1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36]

# Espacio muestral de dos dados
resultados = [i+j for i in range(1,7) for j in range(1,7)]

# Distribución teórica de la variable aleatoria suma
suma_dados, frec_teorica = np.unique(resultados,return_counts=True)
prob_teorica = frec_teorica / 36  #(6x6)

# Mostrar la distribución teórica
print("Suma de los dados:", suma_dados)
print("Probabilidad teórica:", prob_teorica)

plt.figure(figsize=(8,5))
plt.bar(var_al,dist_probabilidad,width=1,color='green',edgecolor='limegreen')
plt.xlabel('Variable aleatoria')
plt.ylabel('Probabilidad teórica')
plt.show()

n = 10000
# Generamos valores para ambos dados
dado_1 = dados(n,252)
dado_2 = dados(n,255)
# Sumamos los valores
suma = np.zeros(n)
for i in range(n):
  suma[i] = dado_1[i] + dado_2[i]

# Distribución empírica
suma_empirica, frec_empirica = np.unique(suma,return_counts=True)
prob_empirica = frec_empirica / n

# Comparar la distribución empírica con la teórica
plt.figure(figsize=(10, 6))
plt.bar(var_al - 0.2, dist_probabilidad, width=0.4, label='Teórica', color='green')
plt.bar(suma_empirica + 0.2, prob_empirica, width=0.4, label='Empírica', color='black')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.title('Comparación entre la distribución teórica y empírica')
plt.legend()
plt.grid(True)
plt.show()


# Generamos valores para ambos dados
_dado = dado_doble(n)


# Distribución empírica
suma2_empirica, frec2_empirica = np.unique(_dado,return_counts=True)
prob2_empirica = frec2_empirica / n

# Comparar la distribución empírica con la teórica
plt.figure(figsize=(10, 6))
plt.bar(var_al - 0.2, dist_probabilidad, width=0.4, label='Teórica', color='green')
plt.bar(suma2_empirica + 0.2, prob2_empirica, width=0.4, label='Empírica', color='black')
plt.xlabel('Usando dado doble (2-12)')
plt.ylabel('Probabilidad')
plt.title('Comparación entre la distribución teórica y empírica')
plt.legend()
plt.grid(True)
plt.show()

