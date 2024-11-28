# Importar el módulo random para generar números aleatorios
import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar el número de intentos
intentos = 0

# Utilizar un bucle while para que el usuario adivine el número
while True:
    # Preguntar al usuario que ingrese su suposición
    suposicion = int(input("Adivina el número secreto (entre 1 y 100): "))

    # Incrementar el número de intentos
    intentos += 1

    # Utilizar operadores lógicos para verificar la suposición
    if suposicion < numero_secreto:
        print("Demasiado bajo!")
    elif suposicion > numero_secreto:
        print("Demasiado alto!")
    else:
        print("¡Felicidades! Adivinaste el número secreto en {} intentos.".format(intentos))
        break

# Utilizar un bucle for para mostrar un mensaje de despedida
for i in range(3):
    print("Hasta luego!")