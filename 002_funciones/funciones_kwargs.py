#argumentos de palabras clave
def crearPersonaje(clase, raza, nombre):
    print(f"{nombre.upper()} es un {clase} de raza {raza}")

crearPersonaje(nombre="Leonidaz", clase="Guerrero", raza="Humano")
crearPersonaje("mago", "elfo", "mandalorian")

#se tiene un diccionario como parametro de entrada
def printKwargs(**kwargs):
    print("\n")
    print("Los atributos del personaje son")

    for clave, valor in kwargs.items():
        print(f"{clave}---->{valor}")

printKwargs(nombre="Leonidaz", clase="Guerrero", raza="Humano", mascota="Dragon", clan="Spartans")
printKwargs(nombre="Mandalorian", clase="MAgo", raza="Elfo")