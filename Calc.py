"""
Eight-Function Calculator with Tkinter UI, History Saving,
Square, Square Root (½ power), Percentage, and Arbitrary Power

Authors: Alek LaBruna, Reece Carew

Description:
    - Supports +, -, *, / operations via a GUI.
    - Supports x², √ (as ^(1/2)), % (percentage), and ^ (power) via buttons.
    - Calculation history is written to "history.txt" and loaded at startup.
    - Demonstrates:
        • Tkinter UI and event loop
        • Functions and modular design
        • Exception handling
        • File I/O for data persistence
        • Use of lists and dictionaries
        • simpledialog for user prompts
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import os

HISTORY_FILE = "history.txt"


def load_history():
    """
    Load previous calculations from HISTORY_FILE.
    Returns a list of history entries.
    """
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return [line.strip() for line in f]


def save_to_history(entry: str):
    """
    Saves a single entry to the history file, creating dir if needed.
    """
    dirpath = os.path.dirname(HISTORY_FILE)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")


def on_button_click(char: str):
    """
    Insert the clicked character (digit or operator) into the display.
    """
    display.insert(tk.END, char)


def clear_display():
    """
    Clear the calculator display.
    """
    display.delete(0, tk.END)


def calculate():
    """
    Evaluate the basic arithmetic expression in the display,
    display the result, and save to history.
    """
    expr = display.get().strip()
    if not expr:
        return
    try:
        # Safe eval context for + - * /
        result = eval(expr, {"__builtins__": None}, {})
        display.delete(0, tk.END)
        display.insert(0, str(result))
        save_to_history(f"{expr} = {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear_display()
    except Exception:
        messagebox.showerror("Error", "Invalid expression.")
        clear_display()


def square():
    """
    Square the number in the display.
    """
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
    save_to_history(f"{expr}^2 = {result}")


def square_root():
    """
    Compute the ½ power (sqrt) of the number in the display.
    """
    expr = display.get().strip()
    if not expr:
        messagebox.showerror("Error", "Enter a number first.")
        return
    try:
        val = float(expr)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for square root.")
        clear_display()
        return
    if val < 0:
        messagebox.showerror("Error", "Cannot take square root of a negative value.")
        clear_display()
        return
    result = val ** 0.5
    display.delete(0, tk.END)
    display.insert(0, str(result))
    save_to_history(f"{expr}^(1/2) = {result}")


def percent():
    """
    Compute percentage (divide by 100) of the current number.
    """
    expr = display.get().strip()
    try:
        val = float(expr)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number before percent operation.")
        clear_display()
        return
    result = val / 100
    display.delete(0, tk.END)
    display.insert(0, str(result))
    save_to_history(f"{expr}% = {result}")


def power():
    """
    Raise the current number to a user selected exponent.
    """
    expr = display.get().strip()
    if not expr:
        messagebox.showerror("Error", "Enter a base number first.")
        return
    try:
        base = float(expr)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid base number.")
        clear_display()
        return
    exp = simpledialog.askfloat("Exponent", "Enter exponent:")
    if exp is None:
        return
    try:
        result = base ** exp
        display.delete(0, tk.END)
        display.insert(0, str(result))
        save_to_history(f"{base}^{exp} = {result}")
    except Exception:
        messagebox.showerror("Error", "Could not compute power operation.")
        clear_display()


def show_history():
    """
    Popup a window displaying full calculation history.
    """
    hist = load_history()
    win = tk.Toplevel(root)
    win.title("History")
    txt = tk.Text(win, width=40, height=15, wrap="word")
    txt.pack(padx=10, pady=10)
    txt.insert("1.0", "\n".join(hist) if hist else "(No history yet)")


# ——— UI Setup ———
root = tk.Tk()
root.title("Calculator with Extended Functions")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 18), bd=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Basic digit and operator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for txt, r, c in buttons:
    cmd = calculate if txt == '=' else lambda ch=txt: on_button_click(ch)
    tk.Button(root, text=txt, width=5, height=2, font=("Arial", 14), command=cmd)\
       .grid(row=r, column=c, padx=5, pady=5)

# Extended function buttons row 5
tk.Button(root, text="x²", width=5, height=2, font=("Arial", 14), command=square)\
   .grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="√½", width=5, height=2, font=("Arial", 14), command=square_root)\
   .grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="%", width=5, height=2, font=("Arial", 14), command=percent)\
   .grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="^", width=5, height=2, font=("Arial", 14), command=power)\
   .grid(row=5, column=3, padx=5, pady=5)

# Control buttons row 6
tk.Button(root, text="Clear", width=5, height=2, font=("Arial", 14), command=clear_display)\
   .grid(row=6, column=0, padx=5, pady=5)
tk.Button(root, text="History", width=5, height=2, font=("Arial", 14), command=show_history)\
   .grid(row=6, column=1, padx=5, pady=5)
# Exit spans two columns for balance
tk.Button(root, text="Exit", width=12, height=2, font=("Arial", 14), command=root.destroy)\
   .grid(row=6, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
