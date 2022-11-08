import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas
import datetime
import os
from tkinter.messagebox import showinfo

class grid(Frame):
    def __init__(self):
        super().__init__()
        self.make_grid()
    def make_grid(self):
        
        canvas = Canvas(self) #important ************************
        canvas = tk.Canvas(root, height=200, width=200, bg='black', highlightthickness=0, borderwidth=0)

        fill_color = "#ffdd00"

        x_start = 10
        y_start = 10
        
        canvas.create_rectangle(x_start, y_start, x_start + 10, y_start + 10, outline="#111111", fill=fill_color) #important
        canvas.pack(fill=BOTH, expand=True)
root = tk.Tk()

ex = grid()


root.configure(bg = "black")
root.mainloop()
