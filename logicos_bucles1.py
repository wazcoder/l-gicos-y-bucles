import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 50)
intentos_maximos = 5
intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He elegido un número entre 1 y 50. Tienes 5 intentos para adivinarlo.")

# Bucle while para permitir hasta 5 intentos
while intentos < intentos_maximos:
    # Pedir al usuario que ingrese su suposición
    suposicion = int(input("Introduce tu suposición: "))
    intentos += 1  # Incrementar el contador de intentos

    # Verificar si la suposición es correcta, demasiado alta o demasiado baja
    if suposicion == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break  # Salir del bucle si adivina correctamente
    elif suposicion < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")

# Si el usuario no adivina en los intentos máximos
if intentos == intentos_maximos and suposicion != numero_secreto:
    print(f"Lo siento, no adivinaste el número. Era {numero_secreto}.")