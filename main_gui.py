import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas
import datetime
import os
from tkinter.messagebox import showinfo

"""
We need TODO:
1) Check the last index of the dataFrame and get the date.
2) Get the day of week, and draw that in the appropriate y coordinate
3) draw the rest of its week
4) draw a blank week in front of it
5) draw 120 days worth of squares behind it.
6) fill in squares as neccesary

^this stuff's all done now
"""

class grid(Frame):
    #a few global variables including: the default dataset (yup, this is mainly what I use this program for), the canvas pointer, and whether or not we're on our first opening of this program
    current_file_name = "leetcode_tracking" 
    canvas = None
    first_open = True
    
    def __init__(self):
        super().__init__()
        self.make_grid()
    
    def get_box_shade(self, cur_val, maximum) -> str:
        #this basically calculates the shade of each square, the lighter the shade, the higher the frequency of an event on said day in proportion to the maximum frequency
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
        elif (0 < pom) & (pom <= 20):
            shade += "052f2f"
        elif (pom <= 0):
            shade += "ffffff"
        else:
            shade = "white"
        return shade

    def open_file_window(self): #for changing datasets
        cd = os.getcwd() 
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir= cd + "/data",
            filetypes=filetypes)
        temp = filename.split("/")[-1]
        temp = temp.split(".")[0]
        
        self.current_file_name = temp
        self.canvas.delete("all")
        self.make_grid()
        
    def make_grid(self): #where the grid itself gets made
        sheet_name = "data/" + self.current_file_name
        df = pandas.read_excel(sheet_name + ".xlsx")
        
        
        #stats #to be implemented later
        """
        maximum
        total
        first_date
        last_date
        days_since_start
        avg_reps_per_day
        """
        #stat collection loop #displaying these will be implemented later.
        maximum = 0
        total = 0
        for i in range(len(df)):
            cur = df.loc[i][1]
            if cur > maximum:
                maximum = cur
            if not pandas.isnull(df.loc[i][2]):
                 total += df.loc[i][2]    
            if not pandas.isnull(df.loc[i][3]):
                 total += df.loc[i][3]
            if not pandas.isnull(df.loc[i][4]):
                 total += df.loc[i][4]   
        
        #we're looking for the day of the week that's last recorded in our spreadsheet
        #the below few lines does that
        first_date = df.loc[0][0] #stats
        last_date = df.loc[len(df) - 1][0] #stats
        
        first_date_split = first_date.split("-")
        first_datetime = datetime.datetime(int(first_date_split[2]), int(first_date_split[0]), int(first_date_split[1]), 0, 0, 0, 0)

        last_date_split = last_date.split("-")
        last_datetime = datetime.datetime(int(last_date_split[2]), int(last_date_split[0]), int(last_date_split[1]), 0, 0, 0, 0)
    
        last_weekday = last_datetime.weekday() #0 = monday  
        



        canvas_height = 220
        canvas_width = 500
        
        self.master.title("Dotter")
        self.pack(fill=BOTH, expand=0)

        if self.first_open: #only initializes canvas the first time you open the program, that way it'll refresh properly when you load a new dataset
            self.canvas = Canvas(self) #important ************************
            #FFDD00 #a nice yellow color
            self.canvas = tk.Canvas(root, height=canvas_height, width=canvas_width, bg='black', highlightthickness=0, borderwidth=0)
            self.first_open = False

            #only make the button the first time it opens
            open_button = tk.Button(
                root,
                text='Select File',
                command=self.open_file_window,
                bg = "white",
                highlightthickness=0,
                borderwidth=0
            )
            #root.bg = "#ffdd00"
            open_button.master.bg = "black"
            open_button.pack(expand=True)
        xpo = 0 #x positional offset #determines current x position for next square
        ypo = 0 #y positional offset #determines current y position for next square

        #grid starting points (for first rectangle)
        gsp_x1 = 22
        gsp_x2 = 42
        gsp_y1 = 22
        gsp_y2 = 42
        square_dim = 20

        cur_day = 0
        cur_data = 0
        ppt_len = len(df)
        grid_width = 18
        grid_height = 7
        original_grid_height = grid_height

        #the loop and associated formulas that draw the grid itself square by square
        for j in range(grid_width, 0, -1):
            xpo = j * square_dim #important
            
            if j == grid_width:
                grid_height = last_weekday + 1
            else:
                grid_height = original_grid_height
                
            for i in range(grid_height, 0, -1):
                ypo = i * square_dim #important

                fill_color = "#fff"
                
                if cur_day < ppt_len:  
                    cur_data = df.loc[ppt_len - 1 - cur_day][1]
                    cur_day += 1
                    fill_color = self.get_box_shade(cur_data, maximum)
                
                self.canvas.create_rectangle(gsp_x1 + xpo, gsp_y1 + ypo, gsp_x2 + xpo, gsp_y2 + ypo, outline="#111111", fill=fill_color) #important

        #draws the date markers on the left of the graph
        date_marker_color = "white"
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 30, anchor=CENTER, font="Purisa",text="M", fill=date_marker_color)
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 70, anchor=CENTER, font="Purisa",text="W", fill=date_marker_color)
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 110, anchor=CENTER, font="Purisa",text="F", fill=date_marker_color)
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 150, anchor=CENTER, font="Purisa",text="S", fill=date_marker_color)
        
        #displays the current file name
        self.canvas.create_text(canvas_width / 2, 15, anchor=CENTER, font="Purisa",text=self.current_file_name + ".xlsx", fill=date_marker_color)
        self.canvas.pack(fill=BOTH, expand=True) #important

        
root = tk.Tk()
ex = grid()

root.configure(bg = "black")
root.mainloop()
