from tkinter import *
from tkinter import messagebox

formulario = Tk()

def infoAyuda():
    messagebox.showinfo("Ayuda", "Si necesitas ayuda puedes ir a www.ponsianodeloor.com")

def infoLicencia():
    messagebox.showwarning("Ayuda", "Licencia MIT www.ponsianodeloor.com")

def cerrarDocumento():
    reintentar = messagebox.askretrycancel("Reintentar", "no es posible cerrar documento bloqueado")

    if reintentar:
        formulario.destroy()

def salirAplicacion():
    salir = messagebox.askquestion("Salir de la aplicacion", "Deseas salir de la aplicacion")

    if salir == "yes":
        formulario.destroy()

def cerrarAplicacion():
    salir = messagebox.askokcancel("Cerrar la aplicacion", "Deseas cerrar de la aplicacion")

    if salir:
        formulario.destroy()

barra_menu = Menu(formulario)
formulario.config(menu=barra_menu, width=300, height=300)

menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()
menu_archivo.add_command(label="Cerrar", command=lambda: cerrarDocumento())
menu_archivo.add_command(label="Salir", command=lambda: salirAplicacion())
menu_archivo.add_command(label="Salir 2", command=lambda: cerrarAplicacion())

menu_edicion = Menu(barra_menu, tearoff=0)
menu_herramientas = Menu(barra_menu, tearoff=0)

menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Licencia", command=lambda: infoLicencia())
menu_ayuda.add_command(label="Acerca de...", command=lambda: infoAyuda())

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edicion", menu=menu_edicion)
barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

formulario.mainloop()