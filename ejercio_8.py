palabra = input("Ingrese una palabra: ")

if len(palabra) % 2 == 0:
    letra_media = palabra[len(palabra)//2 - 1]
else:
    letra_media = palabra[len(palabra)//2]

primera_letra = palabra[0]
ultima_letra = palabra[-1]

print(f"{primera_letra}, {letra_media}, {ultima_letra}")