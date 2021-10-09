from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess



root = tk.Tk()
root.title("Calculator")

def OpenCalculator():
    subprocess.call(["python", "CalculatorSI.py"])

def OpenNote():
    subprocess.call(["python", "NotepadSI.py"])

calculator = ttk.Button(root, text="Calculator", command=lambda: OpenCalculator())
textEditor = ttk.Button(root, text="NotePad", command=lambda: OpenNote())
close = ttk.Button(root, text="Close", command=root.destroy)
calculator.grid(row=1, column=0)
textEditor.grid(row=1, column=1)
close.grid(row=2, column=0, columnspan=2)

root.mainloop()