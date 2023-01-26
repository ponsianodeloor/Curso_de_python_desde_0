from tkinter import *

formulario = Tk()

mi_frame = Frame(formulario, width=500, height=200)

#empaquetar para pertenezca al formulario
mi_frame.pack()

lbl_name = Label(mi_frame, text="Nombre:")
lbl_name.grid(row=0, column=0, sticky="e", padx=10, pady=10)

txt_name = Entry(mi_frame)
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

lbl_name.pack
txt_name.pack


formulario.mainloop()