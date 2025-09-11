#%%
import numpy as np # pyright: ignore[reportMissingModuleSource]
from mis_funciones import gf
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]
x=gf(10000,239)
M=2**32
print(x)
med_muestral=sum(x)/len(x)
dv_muestral=np.std(x)
dv_teorica=np.sqrt(1/12)

numeros=gf(1000,239)

x = numeros[:-1]
y = numeros[1:]
plt.plot(x,y,'ro', label="GF",markersize=1)
plt.xlabel(r"$n_{i}$")
plt.ylabel(r"$n{i+1}$")    
plt.legend()   

print("Media Muestral:")
print(med_muestral)
print("Desviación estándar muestral:")
print(dv_muestral)
print("Desviación estándar teórica (Uniforme[0,1]):")
print(dv_teorica)

#%%
import numpy as np # pyright: ignore[reportMissingModuleSource]
plt.hist(x, bins=30, density=True, color='green', edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma de números pseudoaleatorios')
plt.show()

r=np.random.random(1000)
plt.hist(r,bins=30,density=True,color="lawngreen",edgecolor="black")
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma de numpy.random')
plt.show()








