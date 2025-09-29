#%%

#-------------------------------------------------a)--------------------------------------------------------#
import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

#Primero nos piden que simulemos 100 observaciones de V.A binomial, 
#para ello podemos hacerlo con el comando np.random.binomial el cual devuelve
#muestras de una distribucion binomial con determinados parametros.

# PARÁMETROS INICIALES
n, p, t = 10, 0.4, 100 
# n = número de ensayos en cada experimento binomial
# p = probabilidad de éxito en cada ensayo  
# t = tamaño de la muestra (número de experimentos binomiales)

# GENERACIÓN DE DATOS
datos = np.random.binomial(n, p, t)
# np.random.binomial(n, p, size) genera "t" números aleatorios
# Cada número representa el conteo de éxitos en "n" ensayos con probabilidad "p"

# CONTEO DE FRECUENCIAS
m, incompleto = np.unique(datos, return_counts=True)
# np.unique(datos, return_counts=True) hace dos cosas:
# m: devuelve los valores únicos que aparecen en "datos"
# incompleto: devuelve cuántas veces aparece cada valor único

# PREPARACIÓN DEL VECTOR DE FRECUENCIAS COMPLETO
v = np.zeros(n+1)
# Creamos un vector de ceros de longitud n+1 (porque los posibles valores van de 0 a n)
# Esto asegura que tengamos una posición para cada posible resultado (0,1,2,...,10)

v[m] = incompleto
# Asignamos las frecuencias contadas a sus posiciones correspondientes
# Ejemplo: si m = [1,3,5] e incompleto = [10,20,15], entonces:
# v[1] = 10, v[3] = 20, v[5] = 15, entonces el valor 1 aparece 10 veces y asi con el resto

# CÁLCULO DE FRECUENCIAS RELATIVAS
frec = v/t
# Convertimos frecuencias absolutas a relativas (dividiendo por el total t)

# PREPARACIÓN PARA LA GRÁFICA
escala = np.arange(n+1)
# Creamos un array [0, 1, 2, ..., 10] para el eje x

# CREACIÓN DEL GRÁFICO
plt.bar(escala, frec, color='green', alpha=0.7)
# Graficamos las barras: escala en x, frecuencias en y

plt.xticks(escala)  # Mostramos todos los valores posibles en el eje x
plt.xlabel('Número de éxitos (x)')
plt.ylabel('Frecuencia relativa')
plt.grid(axis='y', alpha=0.3)
plt.title('Distribución Binomial B(10, 0.4)')
plt.show()

#-------------------------------------------b)----------------------------------------------------------
#%%
import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

#Ahora para calcular el valor de chi**2 tenemos la formula chi**2=sum{i,n}(observado_i-esperado)/esperado


# CÁLCULO DE PROBABILIDADES TEÓRICAS
x = np.arange(n+1)  # [0, 1, 2, ..., 10] - todos los valores posibles
teo = sp.binom.pmf(x, n, p)  # Probabilidad teórica para cada valor, o sea nos devuelve la probabilidad de obtener "x" exitos en "n" ensayos 

plt.bar(escala,frec,color='green',alpha=0.7,label='Empirica')
plt.bar(x,teo,facecolor='none',edgecolor='black',alpha=0.7,label='Teorica')
plt.xlabel('Numero de éxitos(x)')
plt.ylabel('Frecuencia relativa')
plt.grid(axis='y',alpha=0.3)
plt.title('Distribucion Binomial teorica vs empirica')
plt.legend()

#Luego, calculamos el estadístico:
a=teo*t #Frecuencia absoluta teórica, pues sp.binom.pmf me devuelve relativas.

chi = 0 #Iniciamos el acumulador del estadistico en 0 
for i in range(len(v)):  #Iteramos sobre todos los valores posibles de 0 a 10 
    chi += ((v[i] - a[i])**2) / a[i]

print('χ² =', chi) #La suma de todas las discrepancias estandarizadas entre lo observado y lo esperado


#--------------------------------------------c)------------------------------------------------------------
#%%
#Para poder decidir si los datos estan de acuerdo al modelo o no podemos realizar una prueba de hipotesis nula
#en donde si el valor de chi**2 que calculamos previamente es menor que el valor de chi**2 critico entonces
#se acepta la hipotesis nula. Entonces eligiendo un nivel de significancia de alpha=0.05 y teniendo 
#9 grados de libertad debido al numero de ensayos que elegimos (en este caso n=10) y a traves del codigo 
#sp.chi2.ppf(1-0.05,n-1) obtenemos el valor 16.9189 y como el valor de chi**2 que calculamos antes era de 9.0788
#entonces quiere decir que debemos aceptar la hipotesis nula que se correspondia con que la simulacion
#sigue el modelo teorico.

print('Valor de chi**2 critico:')
print(sp.chi2.ppf(1-0.05, n-1))

#------------------------------------------------d)--------------------------------------------------------

#%%
#Esto lo podemos calcular con el comando sp.chi2.sf que es la funcion supervivencia evaluada en "x" (buscar en wikipedia)
#donde si el valor de p es mayor al valor alpha elegido entonces no rechazamos la hipotesis nula, como en este
#caso tenemos que p=0.5246 y alpha=0.05 entonces no rechazamos la hipotesis nula.
p = sp.chi2.sf(chi, n)
print(p)

#---------------------------------------------e)------------------------------------------------------------

#%%

chifacil, pfacil = sp.chisquare(v, a) #Acá estamos realizando el test de chi**2 con la tarea sp.chisquare
#de los datos observados y esperados que definimos previamente donde esto seria el camino "facil" o directo
#una vez que ya sabemos la teoria y simplemente queremos calcular de forma directa los valores de chi**2 y 
#de p.
print('El valor de χ² es', chifacil, 'y el p-valor es', pfacil)

mu = np.linspace(2,7,100) #Creamos 100 valores de mu (media de la normal) entre 2 y 7
chig=[]
pg=[]

for i in range(100):
    gauss = np.random.normal(loc=mu[i], scale=2.5, size=1000)#Generamos datos de una distribucion Normal(mu,sigma=2.5)
    gauss_discreto = np.histogram(gauss, bins=11, range=(-0.5,10.5))#Tomamos los datos continuos de la Normal y los discretizamos de 0 a 10
    gauss_discreto=np.array(gauss_discreto[0]/np.sum(gauss_discreto[0]))
    l, k = sp.chisquare(gauss_discreto, teo)#Comparamos los datos normales discretizados con la binomial teorica
    chig.append(l)
    pg.append(k)

plt.show()

plt.plot(mu,pg,'o')
plt.xlabel('Mu')
plt.ylabel('P-valor')
plt.axhline(pfacil, color='black', label='P-valor Binomial (n=10)')

plt.fill_between(mu, 0, pfacil, color='red', alpha=0.2)
plt.fill_between(mu, pfacil, 1, color='green', alpha=0.2)
plt.title('P-valor vs Mu para la Distribución Normal')
plt.legend()
plt.show()


#------------------------------------------------f)----------------------------------------------------------
# %%
import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt
# PARÁMETROS INICIALES
j, k, l = 1000, 0.4, 10000 

# GENERACIÓN DE DATOS
muestra = np.random.binomial(j, k, l)

# CONTEO DE FRECUENCIAS
c, incompleto_ = np.unique(muestra, return_counts=True)

# PREPARACIÓN DEL VECTOR DE FRECUENCIAS COMPLETO
z = np.zeros(j+1)

z[c] = incompleto_

# CÁLCULO DE FRECUENCIAS RELATIVAS
frec_ = z/l

# PREPARACIÓN PARA LA GRÁFICA
escala_ = np.arange(j+1)

# CREACIÓN DEL GRÁFICO
#plt.bar(escala_, frec_,width=0.7, color='blue', alpha=0.7)
#plt.xlim(325,475)
#plt.xlabel('Número de éxitos (x)')
#plt.ylabel('Frecuencia relativa')
#plt.grid(axis='y', alpha=0.3)
#plt.title('Distribución Binomial B(10, 0.4) - Frecuencias Observadas')
#plt.show()

# CÁLCULO DE PROBABILIDADES TEÓRICAS
x_ = np.arange(j+1)  # [0, 1, 2, ..., 1000] - todos los valores posibles
teo_ = sp.binom.pmf(x_, j, k)  # Probabilidad teórica para cada valor, o sea nos devuelve la probabilidad de obtener "x" exitos en "n" ensayos 

b=teo_*l

chifacil_,pfacil_=sp.chisquare(z,b)

# SOLUCIÓN: FILTRAR Y NORMALIZAR
print("=== FILTRANDO CATEGORÍAS ===")
print(f"Total de categorías posibles: {len(b)}")

# Filtrar solo categorías con frecuencia esperada suficiente
indices_validos = b >= 1

z_filtrado = z[indices_validos]
b_filtrado = b[indices_validos]
x_filtrado = x_[indices_validos]

# CORRECCIÓN: VERIFICAR SUMAS
suma_observados = np.sum(z_filtrado)
suma_esperados = np.sum(b_filtrado)


# SOLUCIÓN: NORMALIZAR LAS FRECUENCIAS ESPERADAS
if abs(suma_observados - suma_esperados) > 1e-8:
    print("⚠️  Normalizando frecuencias esperadas...")
    factor_normalizacion = suma_observados / suma_esperados
    b_filtrado_normalizado = b_filtrado * factor_normalizacion
    print(f"Factor de normalización: {factor_normalizacion}")
else:
    b_filtrado_normalizado = b_filtrado

# APLICAR TEST CHI-CUADRADO
if np.sum(indices_validos) >= 2:
    chifacil_, pfacil_ = sp.chisquare(z_filtrado, b_filtrado_normalizado)
    print(f" RESULTADO DEL TEST:")
    print(f"χ² = {chifacil_:.4f}")
    print(f"p = {pfacil_:.4f}")


print(f"χ²_critico={sp.chi2.ppf(1-0.05, j-1)}")

#%%
#Ahora si intentamos recrear el inciso anterior(queda por terminar, empiezo el informe)    
   
mu_ = np.linspace(2,7,1000) #Creamos 100 valores de mu (media de la normal) entre 2 y 7
chig_=[]
pg_=[]

for i in range(100):
    gauss_ = np.random.normal(loc=mu_[i], scale=2.5, size=1000)#Generamos datos de una distribucion Normal(mu,sigma=2.5)
    gauss_discreto = np.histogram(gauss_, bins=50, range=(350,450))#Tomamos los datos continuos de la Normal y los discretizamos de 0 a 10
    gauss_discreto=np.array(gauss_discreto[0]/np.sum(gauss_discreto[0]))
    h, j = sp.chisquare(gauss_discreto, teo)#Comparamos los datos normales discretizados con la binomial teorica
    chig_.append(h)
    pg_.append(j)

#%%


