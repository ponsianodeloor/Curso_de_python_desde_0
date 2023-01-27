from tkinter import *

formulario = Tk()

formulario.title("Check button")

"""
photo = PhotoImage(file="avion.png")
Label(formulario, image=photo).pack()
"""

playa = IntVar()
montana = IntVar()
turismo_rural = IntVar()

def opcionesViajes():
    opcionSeleccionada = ""

    if playa.get() == 1:
        opcionSeleccionada+="Playa"

    if montana.get() == 1:
        opcionSeleccionada+="MOntaña"

    if turismo_rural.get() == 1:
        opcionSeleccionada+="Turismo Rural"

    print(opcionSeleccionada)
    texto_final.config(text=opcionSeleccionada)


mi_frame = Frame(formulario)
mi_frame.pack()

Label(mi_frame, text="Elige Destinos", width=50).pack()
Checkbutton(mi_frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=lambda:opcionesViajes()).pack()
Checkbutton(mi_frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=lambda:opcionesViajes()).pack()
Checkbutton(mi_frame, text="Turismo Rural", variable=turismo_rural, onvalue=1, offvalue=0, command=lambda:opcionesViajes()).pack()

texto_final = Label(mi_frame)
texto_final.pack()

formulario.mainloop()