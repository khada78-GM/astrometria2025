#%%
import numpy as np
def simular_buffon(N, l, t):

    cruces = 0  # Contador de cuántas veces la aguja toca una raya

    for _ in range(N):
        x = np.random.uniform(0, t/2)  # Distancia a la raya más cercana
        theta = np.random.uniform(0, np.pi/2)  # Ángulo agudo con las rayas

        # Condición para que la aguja cruce una raya
        if (l/2) * np.sin(theta) > x:
            cruces += 1

    # Estimar pi usando la fórmula de Buffon
    pi_est = (2 * l * N) / (t * cruces)
    return pi_est

# Parámetros
N = 100000  # Número de simulaciones
l = 29  # Longitud de la aguja
t = 30  # Separación entre las rayas (debe ser mayor que l)

# Realizar la simulación
pi_estimado = simular_buffon(N, l, t)

# Mostrar resultado
print(f"Estimación de pi después de {N} lanzamientos: {pi_estimado}")

# Comparar con el valor real de pi
print(f"Valor real de pi: {np.pi}")
