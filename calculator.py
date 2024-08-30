import tkinter as tk  # Import tkinter with alias tk

root = tk.Tk()  # Initialize the main window
root.title("Simple Calculator")  # Set the window title

expression = ""

def add(value):
    global expression
    expression += value
    label_result.config(text=expression)

def clear():
    global expression
    expression = ""
    label_result.config(text="")

def calculate():
    global expression
    try:
        result = eval(expression)
        label_result.config(text=str(result))
        expression = str(result)
    except Exception as e:
        label_result.config(text="Error")
        expression = ""

label_result = tk.Label(root, text="", font=('Helvetica', 16), bg='white', padx=10, pady=10)
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", width=15, command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", width=15, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", width=15, command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = tk.Button(root, text="/", width=15, command=lambda: add("/"))
button_divide.grid(row=1, column=3)

button_4 = tk.Button(root, text="4", width=15, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", width=15, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", width=15, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tk.Button(root, text="*", width=15, command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

button_7 = tk.Button(root, text="7", width=15, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", width=15, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", width=15, command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_subtract = tk.Button(root, text="-", width=15, command=lambda: add("-"))
button_subtract.grid(row=3, column=3)

button_clear = tk.Button(root, text="C", width=15, command=clear)
button_clear.grid(row=4, column=0)

button_0 = tk.Button(root, text="0", width=15, command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tk.Button(root, text=".", width=15, command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = tk.Button(root, text="+", width=15, command=lambda: add("+"))
button_add.grid(row=4, column=3)

button_equals = tk.Button(root, text="=", width=25, command=calculate)
button_equals.grid(row=5, column=0, columnspan=4)

root.mainloop()  # Run the application loop
