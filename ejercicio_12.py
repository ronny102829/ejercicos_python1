cantidad_numeros = int(input("¿Cuántos números va a introducir? "))
contador_negativos = 0

for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    if numero < 0:
        contador_negativos += 1

print(f"Ha introducido {contador_negativos} número(s) negativo(s).")