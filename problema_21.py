#Tenemos que hacer el juego de monty hall

#%%
import numpy as np # pyright: ignore[reportMissingImports]
def jugar_monty_hall():
  # Inicializa las puertas: 0 representa cabra, 1 representa auto
  puertas = [0, 0, 0]
  # Selecciona aleatoriamente la puerta que tendrá el auto
  auto = np.random.randint(0, 2)
  puertas[auto] = 1
  print(f"[DEBUG] Puertas: {puertas} (1 es auto, 0 es cabra)")
  print(f"[DEBUG] El auto está en la puerta {auto}")

  # Mensaje de bienvenida y explicación del juego
  print("Bienvenido al juego Monty Hall.")
  print("Hay 3 puertas: 0, 1 y 2. Una tiene un auto, las otras cabras.")
  # El jugador elige una puerta
  eleccion = int(input("Elige una puerta (0, 1 o 2): "))
  print(f"[DEBUG] Elegiste la puerta {eleccion}")
 
  

  # El presentador busca una puerta con cabra que no haya sido elegida
  opciones_restantes = []
  for i in range(3):
    # Si la puerta no es la elegida y tiene cabra, se agrega a las opciones
    if i != eleccion and puertas[i] == 0:
      opciones_restantes.append(i)
  print(f"[DEBUG] Puertas que puede abrir el presentador (cabras y no elegidas): {opciones_restantes}")

  # El presentador abre una de las puertas con cabra
  abierta = np.random.choice(opciones_restantes)
  print(f"El presentador abre la puerta {abierta}, ¡hay una cabra!")
  print(f"[DEBUG] Puerta abierta por el presentador: {abierta}")

  # El jugador decide si quiere cambiar su elección
  opcion = input("¿Quieres cambiar tu elección? (s/n): ").lower()
  print(f"[DEBUG] Opción de cambiar: {opcion}")

  # Condicional: si el jugador decide cambiar
  if opcion == 's':
    # Busca la puerta que no fue elegida ni abierta por el presentador
    for i in range(3):
      if i != eleccion and i != abierta:
        nueva_eleccion = i
    print(f"[DEBUG] Cambiaste tu elección a la puerta {nueva_eleccion}")
    eleccion = nueva_eleccion
  else:
    # Si el jugador no cambia, mantiene su elección original
    print(f"[DEBUG] Te quedaste con la puerta {eleccion}")

  # Condicional: verifica si la puerta elegida tiene el auto
  if puertas[eleccion] == 1:
    print("¡Ganaste el auto!")
    print(f"[DEBUG] Puerta final {eleccion} tiene el auto.")
  else:
    print("¡Te llevaste una cabra!")
    print(f"[DEBUG] Puerta final {eleccion} tiene una cabra.")

# Punto de entrada principal del programa
if __name__ == "__main__":
  jugar_monty_hall()
