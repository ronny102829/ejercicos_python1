cantidad_numeros = int(input("¿Cuántos números va a introducir? "))
suma = 0

for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero

print(f"La suma de los números introducidos es: {suma}")