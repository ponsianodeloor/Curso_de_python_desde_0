import tkinter.messagebox
from tkinter import *



formulario = Tk()

tkMessageBox = tkinter.messagebox

mi_frame = Frame(formulario, width=500, height=200)

#empaquetar para pertenezca al formulario
mi_frame.pack()

mi_nombre = StringVar()

lbl_name = Label(mi_frame, text="Nombre:")
lbl_name.grid(row=0, column=0, sticky="e", padx=10, pady=10)

txt_name = Entry(mi_frame, textvariable=mi_nombre)
txt_name.grid(row=0, column=1, padx=10, pady=10)
txt_name.config(fg="red", justify="center")

lbl_lastname = Label(mi_frame, text="Apellido:")
lbl_lastname.grid(row=1, column=0, sticky="e", padx=10, pady=10)

txt_lastname = Entry(mi_frame)
txt_lastname.grid(row=1, column=1, padx=10, pady=10)

lbl_address = Label(mi_frame, text="Direccion de la casa:")
lbl_address.grid(row=2, column=0, sticky="e", padx=10, pady=10)

txt_address = Entry(mi_frame)
txt_address.grid(row=2, column=1, sticky="e", padx=10, pady=10)

lbl_password = Label(mi_frame, text="Password:")
lbl_password.grid(row=3, column=0, sticky="e", padx=10, pady=10)

txt_password = Entry(mi_frame)
txt_password.grid(row=3, column=1, padx=10, pady=10)
txt_password.config(show="*")

lbl_comentarios = Label(mi_frame, text="Comentarios:")
lbl_comentarios.grid(row=4, column=0, sticky="e", padx=10, pady=10)

txt_comentarios = Text(mi_frame, width=16, height=5)
txt_comentarios.grid(row=4, column=1, padx=10, pady=10)

#colocando un scrollbar en el textarea
scroll_vertical_txt_comentarios = Scrollbar(mi_frame, command=txt_comentarios.yview)
scroll_vertical_txt_comentarios.grid(row=4, column=2, sticky="nsew")

scroll_vertical_txt_comentarios.pack
#txt_password.config(yscrollcommand=scroll_vertical_txt_comentarios.set)

""""
# Add a Scrollbar(vertical)
v=Scrollbar(formulario, orient='vertical')
v.pack(side=RIGHT, fill='y')

# Add a text widget
text=Text(formulario, yscrollcommand=v.set, width=16, height=5)
#text.grid(row=5, column=2)

# Attach the scrollbar with the text widget
v.config(command=text.yview)
text.pack()
"""

def saludar():
  tkMessageBox.showinfo("Saludos", "Hello Python")
  mi_nombre.set("Ponsiano")


btn_envio = Button(formulario, text="Enviar", command=saludar())
btn_envio.place(x=50, y=50)
btn_envio.pack


lbl_name.pack
txt_name.pack

formulario.mainloop()