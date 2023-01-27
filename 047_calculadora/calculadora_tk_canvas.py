import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

numero=tk.StringVar()
entry2 = tk.Entry(root, textvariable=numero)
canvas1.create_window(350, 180, window=entry2)




def get_square_root():
    x1 = entry1.get()

    label1 = tk.Label(root, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)

    numero.set(7)


button1 = tk.Button(text='Get the Square Root', command=get_square_root)
canvas1.create_window(200, 180, window=button1)

root.mainloop()