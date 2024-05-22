# - *Ejercicio Diecisiete*
# > Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
# > 
# > - Verificar el saldo de su cuenta.
# > - Depositar dinero en su cuenta.
# > - Retirar dinero de su cuenta.
# > - Salir del programa.
# > El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
# > 
# > - Verificar saldo
# > - Depositar dinero
# > - Retirar dinero
# > - Salir
saldo= 15190
while True:
    print("\cajero automatico bcp")
    print(f"""usted cuenta con{saldo}s/ en su cuenta 
1.Verificar el saldo de su cuenta.
2. Depositar dinero en su cuenta.
3.Retirar dinero de su cuenta.
4. salir """)
    opcion=int(input("ingresar opcion->>"))
    if  opcion == 1:
        print(f"\nusted{saldo}s/ en su cuenta\n")
    if opcion == 2:
        print("cundo de money desea ingresar")
        deposito=int(input())
        saldo+=deposito
        print(f"\nse sea realisodo un imgresi{saldo}s/ actualmente cuenta con {deposito}s/ en su cuenta\n")
    if opcion == 3:
        print("cuanto de dinerop desea retirar")
        retiro=int(input())
        saldo+=retiro
        print(f"\nusted retiro{retiro}s/ actualmente cuenta con {saldos}s/\n")
    if opcion == 4:
        print("greacias por su viSITA")
        break
#