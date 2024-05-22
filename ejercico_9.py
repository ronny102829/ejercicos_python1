cantidad_numeros = int(input("¿Cuántos números va a introducir? "))
anterior = float(input("Ingrese el primer número: "))

for i in range(1, cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    if numero <= anterior:
        print(f"El número {numero} no es mayor que el anterior ({anterior}).")
    anterior = numero