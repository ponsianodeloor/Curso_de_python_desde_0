from tkinter import *
from tkinter import filedialog

formulario = Tk()

def abrirArchivo():
    archivos = (
        ("Imagenes", "*.jpg",),
        ('Acrobat', '*.pdf')
    )
    fichero = filedialog.askopenfilename(title="Abrir", filetypes=(archivos))
    print(fichero)

Button(formulario, text="Abrir archivo", command=lambda:abrirArchivo()).pack()

formulario.mainloop()