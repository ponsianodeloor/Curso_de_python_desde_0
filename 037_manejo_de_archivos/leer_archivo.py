from io import open

leer_archivo = open("archivo.txt", "r")

ver_texto = leer_archivo.read()

leer_archivo.close()

print(ver_texto)