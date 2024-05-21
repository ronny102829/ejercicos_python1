# jercicio Trece**
#  Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.
#  
#  Esta calculadora funciona de la siguiente manera:
#  
#  - Recogemos los datos A y B
#  - Si operación es 1 calcula la raíz cuadrada de la suma de A y B
#  - Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
#  - Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
while True:
    print("calculadora")
    entrada_a=int(input("intuducir valor A->> "))
    entrada_b=int(input("intuducir valor B->> "))
    print("""1. calcula la raíz cuadrada de la suma de A y B
2.calcula A / B. Vigilamos que B no sea 0...
3. calculamos ( A * B ) / 2.5  """)
    opcion=int(input("ingrese obcion->>"))
    if opcion == 1:
        print
      