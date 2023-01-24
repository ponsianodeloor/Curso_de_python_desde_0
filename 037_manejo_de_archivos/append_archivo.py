from io import open

archivo = open("archivo.txt", "a")

informacion_adicional = "Estamos estudiando py el objetivo es comprender django y fastApi"
ver_texto = archivo.write(informacion_adicional)

archivo.close()