from tkinter import *

formulario = Tk()

opcion = IntVar()

def imprimir():
    print(opcion.get())
    if opcion.get() == 1:
        etiqueta.config(text="Has elegido Masculino")
    else:
        etiqueta.config(text="Has elegido Femenino")



Label(formulario, text="Genero:").pack()
Radiobutton(formulario, text="Masculino", variable=opcion, value=1, command=lambda: imprimir()).pack()
Radiobutton(formulario, text="Femenino", variable=opcion, value=2, command=lambda: imprimir()).pack()

etiqueta = Label(formulario)
etiqueta.pack()

formulario.mainloop()