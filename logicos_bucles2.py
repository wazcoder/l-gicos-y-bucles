# Preguntar al usuario cuántos números quiere sumar
numeros_a_sumar = int(input("¿Cuántos números quieres sumar? "))

# Inicializar la suma
suma = 0

# Utilizar un bucle for para sumar los números
for i in range(numeros_a_sumar):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    suma += numero

# Utilizar un bucle while para mostrar los resultados
i = 1
while i <= numeros_a_sumar:
    print("Número {}: {}".format(i, numero))
    i += 1

# Mostrar la suma
print("La suma es: {}".format(suma))