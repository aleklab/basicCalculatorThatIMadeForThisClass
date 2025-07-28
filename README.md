# basicCalculatorThatIMadeForThisClass

## Description

This project is a **GUI-based calculator** built with Python and Tkinter. It supports basic arithmetic operations and several advanced functions, and it saves a history of calculations to a text file. It demonstrates:

* Event-driven UI with Tkinter
* Modular functions and exception handling
* File I/O for data persistence
* Use of built-in and standard libraries

## Features

1. **Basic Operations**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`).
2. **Square**: Compute the square of the number (`x²`).
3. **Square Root**: Compute the square root using the exponent `^(1/2)`.
4. **Percentage**: Convert a number to its percentage (`%` divides by 100).
5. **Arbitrary Power**: Prompt the user for an exponent and raise the base to that power (`^`).
6. **Calculation History**:

   * Loads previous history from `history.txt` on startup.
   * Stores each new calculation to `history.txt`.
   * Displays full history in a pop-up window.
     
7. **Error Handling**:

   * Handles invalid inputs, division by zero, and negative square root requests.

## External Libraries

* **tkinter** (built-in): For GUI components, dialogs, and event loop.
* **os** (built-in): To check and manage the history file.
* **tkinter.messagebox**: For error messages.
* **tkinter.simpledialog**: For prompting the user for input.

No third-party packages are required.

## Requirements

* Python 3.6 or higher
* Standard library only (no external dependencies)

## Installation

1. **Clone repo**
   
   * "git clone https://github.com/aleklab/basicCalculatorThatIMadeForThisClass.git"
   * "cd basicCalculatorThatIMadeForThisClass"
     
2. **Run program**

   * "python calc.py"


**Using the Calculator**:

   * Click buttons or type expressions directly into the display.
   * Use `=` to evaluate, `Clear` to reset, and `Exit` to close.
   * Click `History` to view all past calculations.


## Authors & Attribution

* **Alek LaBruna**
* **Reece Carew**

