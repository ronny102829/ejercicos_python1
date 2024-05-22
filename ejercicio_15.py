# - *Ejercicio Quince*
# > Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
# > 
# >  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# > 
# > Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.-
numero_uno,numero_dos=0,1
while numero_dos < 90:
    print(numero_uno,numero_dos,end=" ")
    numero_uno+=numero_dos
    numero_dos+=numero_uno
    #