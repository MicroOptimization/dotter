import tkinter as tk
from tkinter import *
import pandas
import datetime

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

"""
We need TODO:
1) Check the last index of the dataFrame and get the date.
2) Get the day of week, and draw that in the appropriate y coordinate
3) draw the rest of its week
4) draw a blank week in front of it
5) draw 120 days worth of squares behind it.
6) fill in squares as neccesary
"""

#def create_grid(event=None):
#    tk.Canvas.create_rectangle(100, 110, 100, 110, fill = "red")


class grid(Frame):
    def __init__(self):
        super().__init__()

        self.make_grid()


    def get_box_shade(self, cur_val, maximum) -> str:
        pom = 100 * (cur_val / maximum) #pom = percentage of max value
        shade = "#"
        
        if (80 < pom) & (pom <= 100):
            shade += "5ff0f2"
        elif (60 < pom) & (pom <= 80):
            shade += "31ebef"
        elif (40 < pom) & (pom <= 60):
            shade += "15babe"
        elif (20 < pom) & (pom <= 40):
            shade += "0d7577"
        elif (0 <= pom) & (pom <= 20):
            shade += "052f2f"
        else:
            shade = shade
        return shade
    
    def make_grid(self):
        sheet_name = "data"
        df = pandas.read_excel(sheet_name + ".xlsx")

        maximum = 0
        for i in range(len(df)):
            if df.loc[i][1] > maximum:
                maximum = df.loc[i][1]
        print("maximum" , maximum)

        

        
        #we're looking for the day of the week that's last recorded in our spreadsheet

        last_date = df.loc[len(df) - 1][0]     
        date_split = last_date.split("-")
        date = datetime.datetime(int(date_split[2]), int(date_split[0]), int(date_split[1]), 0, 0, 0, 0)
        last_weekday = date.weekday() #0 = monday
        #print("lwd:" , last_weekday)
        
        #print(last_date)

        


        
        self.master.title("Dotter")
        self.pack(fill=BOTH, expand=0)

        canvas = Canvas(self) #important ************************

        
        xpo = 0 #x positional offset
        ypo = 0 #y positional offset

        #grid starting points (for first rectangle)
        gsp_x1 = 22
        gsp_x2 = 42
        gsp_y1 = 22
        gsp_y2 = 42
        square_dim = 20
        #canvas.create_rectangle(2, 2, 52, 52, outline="#111111", fill="#fb0")

        #get_box_shade(cur_val, maximum)

        #print(df.loc[cur_day][1]) #column 1 (column is 2nd index of loc)
        cur_day = 0
        cur_data = 0
        ppt_len = len(df)
        grid_width = 18
        for j in range(grid_width, 0, -1):
            xpo = j * square_dim #important
            for i in range(7, 0, -1):
                ypo = i * square_dim #important

                fill_color = "#fb0"
                
                if cur_day < ppt_len:  
                    cur_data = df.loc[ppt_len - 1 - cur_day][1]
                    #print(cur_data)
                    cur_day += 1
                    fill_color = self.get_box_shade(cur_data, maximum)
                
                
                canvas.create_rectangle(gsp_x1 + xpo, gsp_y1 + ypo, gsp_x2 + xpo, gsp_y2 + ypo, outline="#111111", fill=fill_color)
                
                #print(gsp_x2 + xpo, gsp_y2 + ypo) #2) final value: 382 162 
                #print(gsp_x1 + xpo, gsp_y1 + ypo) #1) final value: 362 142
        canvas.pack(fill=BOTH, expand=0)

root = tk.Tk()



ex = grid()

c = tk.Canvas(root, height=180, width=500, bg='white')
c.pack(fill=tk.BOTH, expand=True)

#c.bind('<Configure>', create_grid)


root.mainloop()



"""
if cur_day > 120:
    fill_color = "#999999"
elif cur_day > 90:
    fill_color = "#666666"
elif cur_day > 60:
    fill_color = "#444444"
elif cur_day > 30:
    fill_color = "#333333"
else:
    fill_color = "#222222"
"""


