from io import open

archivo = open("archivo.txt", "w")

frase = "Estupendo dia para estudiar py \n hoy es miercoles"

archivo.write(frase)

archivo.close()