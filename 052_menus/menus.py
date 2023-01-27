from tkinter import *

formulario = Tk()

barra_menu = Menu(formulario)
formulario.config(menu=barra_menu, width=300, height=300)

menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()
menu_archivo.add_command(label="Cerrar")
menu_archivo.add_command(label="Salir")

menu_edicion = Menu(barra_menu, tearoff=0)
menu_herramientas = Menu(barra_menu, tearoff=0)

menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Licencia")
menu_ayuda.add_command(label="Acerca de...")

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edicion", menu=menu_edicion)
barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

formulario.mainloop()