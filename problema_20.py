#%%
from mis_funciones import gpa
from mis_funciones import gf
import numpy as np

# Función corregida sin números ni puntos sobrantes
def pearson_correlation(x, y):
    """
    Calcula el coeficiente de correlación de Pearson entre dos arrays
    """
    if len(x) != len(y):
        raise ValueError("Los arrays deben tener la misma longitud")

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sqrt(
        np.sum((x - mean_x)**2) * 
        np.sum((y - mean_y)**2)
    )

    return numerator / denominator if denominator != 0 else 0


# Lista de retardos
retardos = [1, 2, 3, 5, 7, 10]
num_con = gpa(1000,10)
num_fibo= gf(1000,10)
# Convertir tus secuencias a arrays de NumPy
arr_con = np.array(num_con)   # tu lista de congruencia lineal
arr_fib = np.array(num_fibo)     # tu lista de Fibonacci con retardo

# Bucle sobre cada retardo
for d in retardos:
    x_con = arr_con[:-d]   # quita los últimos d elementos
    y_con = arr_con[d:]    # quita los primeros d elementos
    r_con = pearson_correlation(x_con, y_con)

    x_fib = arr_fib[:-d]

    y_fib = arr_fib[d:]
    r_fib = pearson_correlation(x_fib, y_fib)

    print(f"Retardo {d:2d} → Pearson Congruencial: {r_con:.5f}, Fibonacci: {r_fib:.5f}") # 

# %%
