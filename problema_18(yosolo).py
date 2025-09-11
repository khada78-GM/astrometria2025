#Primero lo que queremos hacer es generar una lista de números aleatorios entre 0 y 1 usando el generador congruencial lineal (GCL). Luego, queremos graficar los pares de números consecutivos (n_i, n_{i+1}) para observar si hay alguna correlación entre ellos. Finalmente, haremos un histograma de los números generados para ver su distribución.
#%% 
from mis_funciones import gpa
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

semilla=10
numeros=gpa(1000,semilla,27,1,256)

print("Lista de numeros generados:")
print(numeros)  #Imprimimos la lista generada

print("Ciclo de repetición:") 
primer_valor = numeros[0]
for i,n in enumerate(numeros[1:],start=2):
    if n==primer_valor:
        print(f"El numero {n} se repite en la posicion {i}")
        break

x = numeros[:-1]
y = numeros[1:]
plt.plot(x,y,'ro', label="GLC",markersize=1)
plt.xlabel(r"$n_{i}$")
plt.ylabel(r"$n{i+1}$")    
plt.legend()   
#%%
#Ahora vamos a calcular el "Momento muestral de orden k" para k=1,3,7 y comparar con el valor esperado 1/(k+1)
#La formula es m_k = 1/n * sum(x_i^k) para i=1 a n
semilla=10
numeros=gpa(1000,semilla)
k=7
n=len(numeros)
m_k=sum(x**k for x in numeros)/n
m_kd=1/(k+1)

print("Momento muestral de orden k-ésimo")
print(m_k)
print("Momento muestral con 1/k+1")
print(m_kd)
#%%
semilla=10
numeros=gpa(1000,semilla)
ks = [1, 3, 7]
n = len(numeros)
resultados = []
for k in ks:
    m_k = sum(x**k for x in numeros) / n
    m_kd = 1 / (k + 1)
    resultados.append(f"k={k}: momento muestral={m_k:.5f}, valor teórico={m_kd:.5f}")

print("Comparación de momentos muestrales y teóricos para k=1,3,7:")
print("\n".join(resultados))
#%%
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]
import numpy as np # pyright: ignore[reportMissingImports]
N_caminatas= 10
N_pasos=1000
x = np.zeros((N_caminatas, N_pasos))
y = np.zeros((N_caminatas, N_pasos))
for i in range(N_caminatas):
    for j in range(1,N_pasos):
        salto = np.random.rand()*2*np.sqrt(2) - np.sqrt(2)
        x[i,j]=x[i,j-1] + salto
        salto = np.random.rand()*2*np.sqrt(2) - np.sqrt(2)
        y[i,j]=y[i,j-1] + salto
plt.plot(x[0],y[0]) #este solamente toma la primera fila del array que hicimos con el np.random.rand
plt.show()#cuando coloco este comando, me muestra la grafica de la primer caminata
for i in range(N_caminatas):
     plt.plot(x[i],y[i])
 #%%
distancia = np.sqrt(x**2+y**2)
for i in range (N_caminatas):
    plt.plot(distancia[i])  
    plt.plot(np.mean(distancia, axis=0), 'black', linewidth=3) 
    