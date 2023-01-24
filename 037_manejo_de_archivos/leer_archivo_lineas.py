from io import open

leer_archivo = open("archivo.txt", "r")

lineas_texto = leer_archivo.readlines()

leer_archivo.close()

print(lineas_texto)
print(lineas_texto[0])
print(lineas_texto[1])