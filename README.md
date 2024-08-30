Simple Calculator Using Tkinter
This is a basic calculator application built using Python's Tkinter library. It features a graphical user interface (GUI) where users can perform basic arithmetic operations such as addition, 
subtraction, multiplication, and division.

Features:
Interactive Interface: The calculator provides an easy-to-use interface with buttons for numbers, operations, and essential functions.
Expression Display: A label at the top of the calculator displays the current expression being input by the user.
Basic Arithmetic Operations: Users can perform addition, subtraction, multiplication, and division using the respective buttons.
Clear Functionality: A 'C' button allows users to clear the current expression and reset the display.
Evaluate Expression: The '=' button evaluates the expression and displays the result.
Error Handling: The calculator handles errors gracefully, displaying "Error" if the expression cannot be evaluated.

Code Structure:
Main Window Initialization: The main window (root) is initialized using Tk() and configured with a title.
Label for Display: A label (label_result) is used to display the current mathematical expression or the result.
Functions:
add(value): Appends a value (number or operator) to the current expression and updates the display.
clear(): Clears the current expression and resets the display to an empty state.
calculate(): Evaluates the current expression using Python's eval() function and updates the display with the result. If an error occurs during evaluation, the display shows "Error."
Button Grid: The calculator's interface is created using a grid of buttons. Each button is linked to a specific function using the command parameter.
Number buttons (0-9) add the corresponding digit to the expression.
Operation buttons (+, -, *, /) append the operation to the expression.
The C button clears the display.
The = button calculates and displays the result.

Usage:
Run the script to launch the calculator window. Click the buttons to input your mathematical expression and press = to see the result. Use the C button to clear the display.
