from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

numero_pantalla=StringVar()
ttk.Entry(frm, textvariable=numero_pantalla).grid(column=2, row=0)

def numeroPulsado(numero):
    numero_pantalla.set(numero)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="4").grid(column=2, row=1)

root.mainloop()