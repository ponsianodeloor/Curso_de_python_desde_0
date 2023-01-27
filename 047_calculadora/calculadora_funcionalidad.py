from tkinter import *

formulario = Tk()

mi_frame = Frame(formulario)

mi_frame.pack()

#---------------pantalla------------
numeroPantalla=StringVar()
pantalla = Entry(mi_frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#pulsaciones teclado
def numeroPulsado(numero):
    numeroPantalla.set(numeroPantalla.get() + numero)

#----------------fila 1-------------
boton_7 = Button(mi_frame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton_7.grid(row=2, column=1, padx=10, pady=10)

boton_8 = Button(mi_frame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton_8.grid(row=2, column=2, padx=10, pady=10)

boton_9 = Button(mi_frame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton_9.grid(row=2, column=3, padx=10, pady=10)

boton_dividir = Button(mi_frame, text="/", width=3)
boton_dividir.grid(row=2, column=4, padx=10, pady=10)

#----------------fila 2-------------
boton_4 = Button(mi_frame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton_4.grid(row=3, column=1, padx=10, pady=10)

boton_5 = Button(mi_frame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton_5.grid(row=3, column=2, padx=10, pady=10)

boton_6 = Button(mi_frame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton_6.grid(row=3, column=3, padx=10, pady=10)

boton_multiplicar = Button(mi_frame, text="*", width=3)
boton_multiplicar.grid(row=3, column=4, padx=10, pady=10)

#----------------fila 3-------------
boton_1 = Button(mi_frame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton_1.grid(row=4, column=1, padx=10, pady=10)

boton_2 = Button(mi_frame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton_2.grid(row=4, column=2, padx=10, pady=10)

boton_3 = Button(mi_frame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton_3.grid(row=4, column=3, padx=10, pady=10)

boton_restar = Button(mi_frame, text="-", width=3)
boton_restar.grid(row=4, column=4, padx=10, pady=10)

#----------------fila 4-------------
boton_1 = Button(mi_frame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton_1.grid(row=4, column=1, padx=10, pady=10)

boton_2 = Button(mi_frame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton_2.grid(row=4, column=2, padx=10, pady=10)

boton_3 = Button(mi_frame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton_3.grid(row=4, column=3, padx=10, pady=10)

boton_restar = Button(mi_frame, text="-", width=3)
boton_restar.grid(row=4, column=4, padx=10, pady=10)

#----------------fila 5-------------
boton_0 = Button(mi_frame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton_0.grid(row=5, column=1, padx=10, pady=10)

boton_coma = Button(mi_frame, text=",", width=3, command=lambda:numeroPulsado("."))
boton_coma.grid(row=5, column=2, padx=10, pady=10)

boton_igual = Button(mi_frame, text="=", width=3)
boton_igual.grid(row=5, column=3, padx=10, pady=10)

boton_suma = Button(mi_frame, text="+", width=3)
boton_suma.grid(row=5, column=4, padx=10, pady=10)

formulario.mainloop()