import tkinter as tk
from tkinter import *
"""
def create_grid(event=None):
    #draws empty grid
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(70, w - 70, 20):
        c.create_line([(i, 30), (i, h - 33)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(30, h - 30, 20):
        c.create_line([(70, i), (w - 73, i)], tag='grid_line')
"""
#def create_grid(event=None):
#    tk.Canvas.create_rectangle(100, 110, 100, 110, fill = "red")


class grid(Frame):
    def __init__(self):
        super().__init__()

        self.make_grid()

    def make_grid(self):
        self.master.title("Dotter")
        self.pack(fill=BOTH, expand=0)

        canvas = Canvas(self)
        xpo = 0 #x positional offset
        ypo = 0 #y positional offset

        #grid starting points (for first rectangle)
        gsp_x1 = 22
        gsp_x2 = 42
        gsp_y1 = 22
        gsp_y2 = 42
        
        #canvas.create_rectangle(2, 2, 52, 52, outline="#111111", fill="#fb0")
        grid_width = 15
        for j in range(grid_width):
            xpo = j * 20
            for i in range(7):
                ypo = i * 20
                fill_color = "#fb0"
                canvas.create_rectangle(gsp_x1 + xpo, gsp_y1 + ypo, gsp_x2 + xpo, gsp_y2 + ypo, outline="#111111", fill=fill_color)
           
        
        #canvas.create_rectangle(2, 50, 52, 100, outline="#111111", fill="#fb0")

        
        
        canvas.pack(fill=BOTH, expand=0)

root = tk.Tk()

ex = grid()

c = tk.Canvas(root, height=180, width=500, bg='white')
c.pack(fill=tk.BOTH, expand=True)

#c.bind('<Configure>', create_grid)


root.mainloop()


