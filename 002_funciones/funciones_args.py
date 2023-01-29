# los valores en args son una lista
def numeroMaximo(*args):
    maximo = args[0]

    for numero in args[1:]:
        if numero > maximo:
            maximo = numero

    return maximo

print(numeroMaximo(10,20,30,40, 60, 70))
print(numeroMaximo(1,2,4,5,3))

def formatoDescargas(tipo, *args):
    cant_args = len(args)

    if tipo=="video":
        if cant_args == 0:
            print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}")
        elif cant_args == 1:
            print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}\n-Resolucion: {args[0]}")
        elif cant_args == 2:
            print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}\n-Resolucion: {args[0]}\n- FPS{args[1]}")
    elif tipo == "audio":
        print(f"El formato seleccionado:\n-Tipo de archivo: {tipo}")
    else:
        print("Formato incorrecto")

formatoDescargas("video")
formatoDescargas("video", 720)
formatoDescargas("video", 1080, 60)


formatoDescargas("audio")