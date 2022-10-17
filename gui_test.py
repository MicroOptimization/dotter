import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(70, w - 70, 20):
        c.create_line([(i, 30), (i, h - 33)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(30, h - 30, 20):
        c.create_line([(70, i), (w - 73, i)], tag='grid_line')

root = tk.Tk()

c = tk.Canvas(root, height=200, width=500, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)

root.mainloop()
