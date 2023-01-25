from io import open

archivo_texto = open("archivo.txt", "r")

print(archivo_texto.read())

archivo_texto.seek(0)

print(archivo_texto.read())

