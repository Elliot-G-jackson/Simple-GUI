from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Main window
window = tk.Tk()
window.title("Text Editor Application")

#Save file system
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")
    
#Open file system
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")   

#set the row and column configurations.
window.rowconfigure(0, minsize=900, weight=1)
window.columnconfigure(1, minsize=900, weight=1)

#widgets for text box, frame and open and save.
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = ttk.Button(fr_buttons, text="Open", command=lambda:open_file())
btn_save = ttk.Button(fr_buttons, text="Save As...", command=lambda:save_file())
btn_close = ttk.Button(fr_buttons, text="Close", command=window.destroy)
#Button locations
btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")
btn_close.grid(row=2, column=0, sticky="ew")

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()