import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas
import datetime
import os
from tkinter.messagebox import showinfo

class grid(Frame):

    canvas = None
    
    def __init__(self):
        super().__init__()
        self.make_grid()

    def remake_grid(self, x, y):

        """
        canvas2 = Canvas(self) #important ************************
        canvas2 = tk.Canvas(root, height=200, width=200, bg='black', highlightthickness=0, borderwidth=0)
    
        x_start = 10
        y_start = 10
        
        canvas2.create_rectangle(x_start, y_start, x_start + 10, y_start + 10, outline="#111111", fill=fill_color) #important
        canvas2.pack(fill=BOTH, expand=True)"""
        print("hi")
        self.canvas.delete("all")


        fill_color = "#ffdd00"
        x_start = x
        y_start = y
        self.canvas.create_rectangle(x_start, y_start, x_start + 10, y_start + 10, outline="#111111", fill=fill_color) #important
        
    def make_grid(self):
        
        self.canvas = Canvas(self) #important ************************
        self.canvas = tk.Canvas(root, height=200, width=200, bg='black', highlightthickness=0, borderwidth=0)
        
        fill_color = "#ffdd00"

        x_start = 10
        y_start = 10
        
        self.canvas.create_rectangle(x_start, y_start, x_start + 10, y_start + 10, outline="#111111", fill=fill_color) #important
        
        new_x = 100
        new_y = 100
        
        redraw_button = tk.Button(
            root,
            text='redraw',
            command = lambda: self.remake_grid(new_x, new_y),
            bg = "white",
            highlightthickness=0,
            borderwidth=0
        )

        
        redraw_button.pack(expand=True)
        self.canvas.pack(fill=BOTH, expand=True)
        
root = tk.Tk()

ex = grid()


root.configure(bg = "black")
root.mainloop()
