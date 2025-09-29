#%%
import matplotlib.pyplot as plt 
import numpy as np
import scipy.stats as stats

#Vamos a realizar el problema 9 "Bootstrap"

n = 30
mean = 2.0
sigma = 1.5
muestra = np.random.normal(mean, sigma, n)
plt.hist(muestra,bins=10, density=True)
plt.title("histograma jaja")
plt.show()

#%%
def bootstrap(x,func, m=1000): #m = numero de remuestreos, conviene escribir "_caracter" a los indices mudos
    y=np.zeros(m)
    for i in range(m):
        _x=np.random.choice(x,size=len(x),replace=True)
        y[i]=func(_x)
    return y
#%%
m=10000
boot= bootstrap(muestra,np.std,m=m)
len(boot)
#%%
plt.hist(boot,bins='auto',color='green',density=True)
plt.xlabel('Varianza')
plt.ylabel('Frecuencia')
plt.vlines(boot.mean(),0,1,color='black',label='Media muestral')
plt.title("Bootstrap de la media")
plt.legend()
plt.show()

#%%
z=(boot-boot.mean())/boot.std()
plt.hist(z,bins='auto',density=True, alpha=0.5)

x=np.linspace(-4,4,1000)
y=stats.norm.pdf(x,0,1)

liminf=stats.norm.ppf(0.025,0,1)
limsup=stats.norm.ppf(0.975,0,1)

mask_left = (x <= liminf)
mask_right = (x >= limsup)

plt.xlabel('Varianza')
plt.ylabel('Frecuencia')
plt.vlines(liminf,0,stats.norm.pdf(liminf,0,1),color='green',label='IC 95%') 
plt.vlines(limsup,0,stats.norm.pdf(limsup,0,1),color='green')
plt.fill_between(x[mask_left], y[mask_left], color="green", alpha=0.3)
plt.fill_between(x[mask_right], y[mask_right], color="green", alpha=0.3)
plt.plot(x,y,color='red',label='normal')
plt.title("Bootstrap de la media estandarizado")
plt.legend()
plt.show()

media=np.mean(boot)
print(media)
# %%
import matplotlib.pyplot as plt 
import numpy as np
import scipy.stats as stats


#Intento de bootstrap con Fisher-Tippett
from mis_funciones import inversa

def bootstrap(x,func, m): #m = numero de remuestreos, conviene escribir "_caracter" a los indices mudos
    y=np.zeros(m)
    for i in range(m):
        _x=np.random.choice(x,size=len(x),replace=True)
        y[i]=func(_x)
    return y

y=np.random.uniform(0,1,10000)
muestra_fish=inversa(y)

m=10000
boot=bootstrap(muestra_fish,np.std,m=m)#Sampleamos 10 mil varianzas de bootstrap
len(boot)

z=(boot-boot.mean())/boot.std() #Normalizamos el remuestreo

x=np.linspace(-4,4,10000)
k=stats.norm.pdf(x,0,1)

liminf_fish=stats.norm.ppf(0.025,0,1)
limsup_fish=stats.norm.ppf(0.975,0,1)
mask_left = (x <= liminf_fish)
mask_right = (x >= limsup_fish)

plt.vlines(liminf_fish,0,stats.norm.pdf(liminf_fish,0,1),color='green',label='IC 95%')
plt.vlines(limsup_fish,0,stats.norm.pdf(limsup_fish,0,1),color='green')
plt.fill_between(x[mask_left], k[mask_left], color='green', alpha=0.8)
plt.fill_between(x[mask_right], k[mask_right], color='green', alpha=0.8)
plt.hist(z,bins='auto',density=True,alpha=0.7)
plt.plot(x,k,color='black',label='Distribucion F-T')
plt.title("Bootstrap Gumbel de la media estandarizada")
plt.legend()

media=np.mean(boot)
media_teorica=(np.pi)**2/6
print('Media teorica:')
print(media_teorica)
print('Media empirica:')
print(media**2)






#%%



