from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Calculator")

expression = ""

def add(value):
    global expression
    expression += value
    labelResult.config(text=expression)
   
def clear():
    global expression 
    expression = ""
    labelResult.config(text=expression)

def calculate():
    global expression
    result = eval(expression)
    labelResult.config(text=result)
    expression = str(result)

#Result Field
labelResult = tk.Label(root, text="")
labelResult.grid(row=0, column=0, columnspan=3)

#Buttons
numOne = ttk.Button(root, text="1", command=lambda: add("1"))
numTwo = ttk.Button(root, text="2", command=lambda: add("2"))
numThree = ttk.Button(root, text="3", command=lambda: add("3"))
numFour = ttk.Button(root, text="4", command=lambda: add("4"))
numFive = ttk.Button(root, text="5", command=lambda: add("5"))
numSix = ttk.Button(root, text="6", command=lambda: add("6"))
numSeven = ttk.Button(root, text="7", command=lambda: add("7"))
numEight = ttk.Button(root, text="8", command=lambda: add("8"))
numNine = ttk.Button(root, text="9", command=lambda: add("9"))
numZero = ttk.Button(root, text="0", command=lambda: add("0"))
equal = ttk.Button(root, text="=", command=lambda: calculate())
clea = ttk.Button(root, text="Clear", command=lambda: clear())
plus = ttk.Button(root, text="+", command=lambda: add("+"))
mis = ttk.Button(root, text="-", command=lambda: add("-"))
times = ttk.Button(root, text="*", command=lambda: add("*"))
divide = ttk.Button(root, text="/", command=lambda: add("/"))
point = ttk.Button(root, text=".", command=lambda: add("."))
close = ttk.Button(root, text="Close", command=lambda: root.destroy())

numOne.grid(row=1, column=0)
numTwo.grid(row=1, column=1)
numThree.grid(row=1, column=2)
numFour.grid(row=2, column=0)
numFive.grid(row=2, column=1)
numSix.grid(row=2, column=2)
numSeven.grid(row=3, column=0)
numEight.grid(row=3, column=1)
numNine.grid(row=3, column=2)
numZero.grid(row=4, column=1)
equal.grid(row=4, column=0)
clea.grid(row=4, column=2)
plus.grid(row=5, column=0)
mis.grid(row=5, column=1)
times.grid(row=5, column=2)
divide.grid(row=6, column=1)
point.grid(row=6, column=0)
close.grid(row=6, column=2)

root.mainloop()
                                                                                                                                