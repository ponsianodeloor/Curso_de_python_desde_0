import tkinter as tk

def evaluate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Error"

def button_press(number):
    current = input_text.get()
    input_text.delete(0, tk.END)
    input_text.insert(0, str(current) + str(number))

def clear():
    input_text.delete(0, tk.END)

def equal():
    result = evaluate(input_text.get())
    input_text.delete(0, tk.END)
    input_text.insert(0, result)

root = tk.Tk()
root.title("Calculator")

input_text = tk.Entry(root, width=35, borderwidth=5)
input_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_0 = tk.Button(root, text="0", padx=10, pady=10, command=lambda: button_press(0)).grid(row=3, column=0)
button_equal = tk.Button(root, text="=", padx=10, pady=10, command=lambda: button_press(0)).grid(row=3, column=0)
button_plus = tk.Button(root, text="=", padx=10, pady=10, command=lambda: button_press(0)).grid(row=3, column=0)

button_1 = tk.Button(root, text="1", padx=10, pady=10, command=lambda: button_press(1)).grid(row=3, column=0)
button_2 = tk.Button(root, text="2", padx=10, pady=10, command=lambda: button_press(2)).grid(row=3, column=1)
button_3 = tk.Button(root, text="3", padx=10, pady=10, command=lambda: button_press(3)).grid(row=3, column=2)

button_4 = tk.Button(root, text="4", padx=10, pady=10, command=lambda: button_press(4)).grid(row=2, column=0)
button_5 = tk.Button(root, text="5", padx=10, pady=10, command=lambda: button_press(5)).grid(row=2, column=1)
button_6 = tk.Button(root, text="6", padx=10, pady=10, command=lambda: button_press(6)).grid(row=2, column=2)

button_7 = tk.Button(root, text="7", padx=10, pady=10, command=lambda: button_press(7)).grid(row=1, column=0)
button_8 = tk.Button(root, text="8", padx=10, pady=10, command=lambda: button_press(8)).grid(row=1, column=1)
button_9 = tk.Button(root, text="9", padx=10, pady=10, command=lambda: button_press(9)).grid(row=1, column=2)

button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: button_press("+"))
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: button_press("-"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_press("*"))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: button_press("/"))
button_equal = tk.Button(root, text="/", padx=41, pady=20, command=lambda: button_press("="))

root.mainloop()
