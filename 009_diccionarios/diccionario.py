mi_diccionario = {
    "Alemania":"Berlin",
    "Francia":"Paris",
    23: "Jordan",
    "Espana":"Madrid"
}

mi_diccionario["Italia"]="Lisboa"
print(mi_diccionario["Alemania"])
print(mi_diccionario)
mi_diccionario["Italia"]="Roma"
print(mi_diccionario)
del mi_diccionario[23]
print(mi_diccionario)

