# numero = int(input("Ingrese un número entero positivo: "))

# impares =(str(num) for num in range(1, numero+1) if num % 2 != 0)

# resultado = ", ".join(impares)
# print("Números impares desde 1 hasta", numero, ":", resultado)


numero = int(input("Ingrese un número entero positivo: "))

impares = [str(num) for num in range(1, numero+1) if num % 2 != 0]

print("Números impares desde 1 hasta", numero, ":", end=" ")
for i in range(len(impares)):
    if i < len(impares) - 1:
        print(impares[i] + ",", end=" ")
    else:
        print(impares[i])