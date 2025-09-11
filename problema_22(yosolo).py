#%%
import numpy as np # pyright: ignore[reportMissingImports]
from mis_funciones import gf
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

    

def generador_galaxias(n):
    galaxias = []
    X = gf(n,142)
    for x in X:
        if (0 <= x) and (x < 0.4):
            galaxias.append("eliptica")
        elif (0.4 <= x) and (x < 0.7):
            galaxias.append("espiral")
        elif (0.7 <=x) and (x < 0.9): 
            galaxias.append("enanas")   
        else:
            galaxias.append("irregular")
    return galaxias    
g=generador_galaxias(10000)      
g_array=np.array(g)
tipos, cantidades=np.unique(g_array, return_counts=True) 
for tipo, cantidad in zip(tipos, cantidades):
     print(f"{tipo}: {cantidad}")
print(g) 

hist=plt.hist(g, bins=4, edgecolor='black')
plt.xlabel('Tipo de galaxia')
plt.ylabel('Cantidad')
plt.title('Distribución de tipos de galaxias')
plt.show()


     