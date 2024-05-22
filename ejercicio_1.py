edad=int(input("ingrese su edad : "))
if edad <4:
    precio="el ingreso gratis"
else:
    if edad<=18:
        precio=5
    else:
        precio=10

print(f"el precio de la entrada es:{precio} soles")

