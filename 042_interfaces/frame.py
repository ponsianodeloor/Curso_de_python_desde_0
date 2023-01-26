from tkinter import *

def centrar(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
    x = (anchura_pantalla // 2) - (anchura//2)
    y = (altura_pantalla//2) - (altura//2)
    r.geometry(f"+{x}+{y}")

formulario = Tk()

formulario.title("Primera Ventana")

#impedir que un formulario no se pueda redimensionar en x ni en y
formulario.iconbitmap("favicon.ico")
formulario.geometry("400x400")
formulario.winfo_screenwidth()
formulario.winfo_screenheight()
formulario.config(bg="purple")

centrar(formulario)

#se debe incrustar el frame dentro del formulario
mi_frame = Frame()
mi_frame.pack(side='right', anchor="n")
mi_frame.config(
    bg="red",
    width=200,
    height=200,
    bd=35,
    relief="groove",
    cursor="pirate"
)


formulario.mainloop()

