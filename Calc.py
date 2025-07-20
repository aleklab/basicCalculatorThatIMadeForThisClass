"""
Six-Function Calculator with Tkinter UI, History Saving,
Square and Square Root Functions

Authors: Alek LaBruna, Reece Carew
Description:
    - Supports +, -, *, / operations via a GUI.
    - Supports x² and √ operations via dedicated buttons.
    - Calculation history is written to "history.txt" and loaded at startup.
    - Demonstrates:
        • Tkinter UI and event loop
        • Functions and modular design
        • Exception handling
        • File I/O for data persistence
        • Use of lists and dictionaries
        • math module for advanced operations
"""

import tkinter as tk
from tkinter import messagebox
import os

HISTORY_FILE = "history.txt"

def load_history():
# Load history from a file, returning a list of entries
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return [line.strip() for line in f]

def save_to_history(entry: str):
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")

def on_button_click(char: str):
    display.insert(tk.END, char)

def clear_display():
    display.delete(0, tk.END)

def calculate():
# Get the expression from the display, evaluate it, and handle errors
    expr = display.get().strip()
    if not expr:
        return
    try:
        result = eval(expr, {"__builtins__": None}, {})
        display.delete(0, tk.END)
        display.insert(0, str(result))
        # Save the expression and result to history
        save_to_history(f"{expr} = {result}")
    # Handle specific exceptions for better user feedback
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear_display()
    except Exception:
        messagebox.showerror("Error", "Invalid expression.")
        clear_display()

def square():
# Square the number in the display, ensuring it's a valid number
    expr = display.get().strip()
    try:
        val = float(expr)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number before squaring.")
        clear_display()
        return

    result = val ** 2
    display.delete(0, tk.END)
    display.insert(0, str(result))
    save_to_history(f"{expr}² = {result}")

def square_root():
# Calculate the square root of the number in the display, ensuring it's valid, and positive
    expr = display.get().strip()
    if not expr:
        messagebox.showerror("Error", "Enter a number first.")
        return

    # ensure it's a valid number
    try:
        val = float(expr)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number before taking square root.")
        clear_display()
        return

    # check for negativity
    if val < 0:
        messagebox.showerror("Error", "Cannot take square root of a negative value.")
        clear_display()
        return

    # compute as val to the 1/2 power
    result = val ** 0.5
    display.delete(0, tk.END)
    display.insert(0, str(result))
    # save history using exponent notation instead of √ since this causes an error
    save_to_history(f"{expr}^(1/2) = {result}")

def show_history():
    hist = load_history()
    win = tk.Toplevel(root)
    win.title("History")
    txt = tk.Text(win, width=40, height=15, wrap="word")
    txt.pack(padx=10, pady=10)
    txt.insert("1.0", "\n".join(hist) if hist else "(No history yet)")

# ——— UI Setup ———

# create main window, gives it a title, and set it to not resizable
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 18), bd=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for txt, r, c in buttons:
    cmd = calculate if txt == '=' else lambda ch=txt: on_button_click(ch)
    tk.Button(root, text=txt, width=5, height=2, font=("Arial", 14),
              command=cmd).grid(row=r, column=c, padx=5, pady=5)

# Extended-function buttons
tk.Button(root, text="x²",    width=5, height=2, font=("Arial", 14),
          command=square).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="√½",    width=5, height=2, font=("Arial", 14),
          command=square_root).grid(row=5, column=1, padx=5, pady=5)

# Control buttons
tk.Button(root, text="Clear",     width=5, height=2, font=("Arial", 14),
          command=clear_display).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="History",   width=5, height=2, font=("Arial", 14),
          command=show_history).grid(row=5, column=3, padx=5, pady=5)
tk.Button(root, text="Exit",      width=23, height=2, font=("Arial", 14),
          command=root.destroy).grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# ——— Start the application ———
root.mainloop()
