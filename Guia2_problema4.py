#%%
#Vamos a realizar ahora la transformada inversa de la distribucion de Poisson
import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as stats

def pdf(t,l):
    
    pdf= l*np.exp(-l*t)
    return pdf  

def cdf(t,l):
    cdf=1-np.exp(-l*t)
    return cdf


def inversa(y,l):
    l=5
    inversa=(-1/l)*np.log(1-y)
    return inversa
#Realizamos una "m" cantidad de ocurrencia entre eventos que queramos y superponemos las curvas
m=5
for i in range(m):
    y=np.random.uniform(0,1,30)
    t=inversa(y,l=5)
    t=np.append(0,t)
    suma_eventos=np.cumsum(t)
    y=len(t)
    plt.plot(np.arange(y),suma_eventos)
plt.xlabel('Eventos')
plt.ylabel('Tiempo (h)')
plt.axhline(3,color='blue')
plt.title('Ocurrencia de eventos')
plt.grid(True)
plt.show