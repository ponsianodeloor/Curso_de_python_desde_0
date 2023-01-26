from tkinter import *

formulario = Tk()

mi_frame = Frame(formulario, width=500, height=200)

#empaquetar para pertenezca al formulario
mi_frame.pack()

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.grid(row=0, column=0)

#empaquetar dentro del frame
cuadro_de_texto = Entry(mi_frame)
cuadro_de_texto.grid(row=0, column=1)

nombre_label.pack
cuadro_de_texto.pack


formulario.mainloop()