# Import tkinter with alias tk
import tkinter as tk 
# Initialize the main window
root = tk.Tk()
# Set the title of the window
root.title("Simple calculator")

#Create a StringVar to hold the current equation
equation = tk.StringVar()
# Create the Entry widget (display area)
display=tk.Entry(root,textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)




# Run the application loop
root.mainloop()





