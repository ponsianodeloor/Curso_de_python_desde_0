from tkinter import *

formulario = Tk()

mi_frame = Frame(formulario, width=500, height=200)

#empaquetar para pertenezca al formulario
mi_frame.pack()

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.place(x=100, y=80)

#empaquetar dentro del frame
cuadro_de_texto = Entry(mi_frame)
cuadro_de_texto.place(x=100, y=100)

nombre_label.pack
cuadro_de_texto.pack


formulario.mainloop()