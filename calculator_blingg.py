import tkinter as tk
import math

# Initialize the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Label for displaying the expression and result
label_result = tk.Label(root, text="", anchor="e", font=("Arial", 24), bg="white", fg="black", bd=10, relief="sunken")
label_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

# Initialize the expression variable to store the input
expression = ""

# Function to add values to the expression
def add(value):
    global expression
    expression += str(value)
    label_result.config(text=expression)

# Function to clear the expression
def clear():
    global expression
    expression = ""
    label_result.config(text="")

# Function to calculate the result
def calculate():
    global expression
    try:
        result = str(eval(expression))
        label_result.config(text=result)
        expression = result
    except:
        label_result.config(text="Error")
        expression = ""

# Function for square root
def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        label_result.config(text=result)
        expression = result
    except:
        label_result.config(text="Error")
        expression = ""

# Function for power (x^y)
def power():
    global expression
    expression += "**"
    label_result.config(text=expression)

# Function for trigonometric sine
def sin():
    global expression
    try:
        result = str(math.sin(math.radians(float(expression))))
        label_result.config(text=result)
        expression = result
    except:
        label_result.config(text="Error")
        expression = ""

# Function for logarithm (base 10)
def log():
    global expression
    try:
        result = str(math.log10(float(expression)))
        label_result.config(text=result)
        expression = result
    except:
        label_result.config(text="Error")
        expression = ""

# Creating buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: add(t) if t != 'C' else clear(), font=("Arial", 18), width=5, height=2).grid(row=row, column=col, padx=5, pady=5)

# Special buttons for scientific functions
tk.Button(root, text="sin", command=sin, font=("Arial", 18), width=5, height=2).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="log", command=log, font=("Arial", 18), width=5, height=2).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="√", command=sqrt, font=("Arial", 18), width=5, height=2).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="^", command=power, font=("Arial", 18), width=5, height=2).grid(row=5, column=3, padx=5, pady=5)

# Equals button
tk.Button(root, text="=", command=calculate, font=("Arial", 18), width=22, height=2).grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Start the main event loop
root.mainloop()

