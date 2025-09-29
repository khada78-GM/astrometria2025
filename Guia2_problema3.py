#método de la transformada inversa
#distribución de Fisher-Tippett

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
#Primero definimos la funcion t(x) siguiendo la distribucion estandar de Gumbel con mu=0 y beta=1 sacado de Wikipedia.
def t(x):
    t=np.exp(-1*x)
    return t
#%%
#Escribimos la PDF respectiva estandar de Gumbel
def pdf(x, b=1 ):
    pdf = b*t(x)*np.exp(-t(x))
    return pdf
#%%
#Calculamos la CDF 
def cdf(x):
    cdf = np.exp(-t(x))
    return cdf

#%%
#De la CDF despejamos "x" en funcion de "y" que vamos a generar una cantidad n de numeros aleatorios distribuidos uniformemente con np.random.uniform entre (0,1)
def inversa(y):
    x = -np.log(-np.log(y))
    return x
# %%
#En el paso anterior definimos la inversa y ahora llevamos a cabo los n numeros aleatorios con np.random.uniform y generamos 100000
y = np.random.uniform(0,1,100000)
x = inversa(y)

# %%
#El comando np.linspace genera un array de N valores igualmente espaciados entre "start" y "stop" y el tercer parametro a definir es la cantidad de numeros que va a equiespaciar entre "start" y "stop".
#Como en este caso nosotros queremos equiespaciar entre "min(x)" y "max(x)" entonces debemos elegir un N grande para que la "Gaussiana" quede "suave".
z = np.linspace(min(x), max(x), 1000)
plt.hist(x,bins='auto',color='green', density=True, label='Histograma empírico')
plt.plot(z, pdf(z), color='black', label='PDF')
plt.title('PDF vs Histograma Empirico')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

#Ahora calculemos la media empirica y la teorica.
b=1
media_teorica=0.57721/b
media = np.mean(x)
print('Media empirica:')
print(media)
print('Media teorica:')
print(media_teorica)

