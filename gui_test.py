import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas
import datetime
import os
from tkinter.messagebox import showinfo

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
    current_file_name = "leetcode_tracking" 
    canvas = None
    first_open = True
    
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
        elif (0 < pom) & (pom <= 20):
            shade += "052f2f"
        elif (pom <= 0):
            shade += "ffffff"
        else:
            shade = shade
        return shade

    def open_file_window(self):
        cd = os.getcwd() 
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        #C:/Users/Codia/Desktop/dotter/dotter/data/auditions.xlsx
        
        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir= cd + "/data",
            filetypes=filetypes)
        temp = filename.split("/")[-1]
        temp = temp.split(".")[0]
        
        self.current_file_name = temp
        print(self.current_file_name)
        self.canvas.delete("all")
        self.make_grid()
        
    def make_grid(self):
        print(self.current_file_name)
        #filename = filedialog.askopenfilename()
        
        sheet_name = "data/" + self.current_file_name
        df = pandas.read_excel(sheet_name + ".xlsx")
        
        
        #stats
        """
        maximum
        total
        first_date
        last_date
        days_since_start
        avg_reps_per_day
        """
        #stat collection
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
        print(total)
        
        #we're looking for the day of the week that's last recorded in our spreadsheet
        #the below few lines does that
        first_date = df.loc[0][0] #stats
        last_date = df.loc[len(df) - 1][0] #stats
        
        first_date_split = first_date.split("-")
        first_datetime = datetime.datetime(int(first_date_split[2]), int(first_date_split[0]), int(first_date_split[1]), 0, 0, 0, 0)

        last_date_split = last_date.split("-")
        last_datetime = datetime.datetime(int(last_date_split[2]), int(last_date_split[0]), int(last_date_split[1]), 0, 0, 0, 0)
    
        last_weekday = last_datetime.weekday() #0 = monday




        ###days_since_start = (last_datetime - first_datetime).days
        #print(days_since_start)
        
        ###avg_reps_per_day = total / days_since_start
        #print(round(avg_reps_per_day, 1))
        
        #print("lwd:" , last_weekday)
        #print("lwd: " , last_weekday)
        #print(last_date)

        #oct 6, = thursday = 3        
        

        canvas_height = 220
        canvas_width = 500
        
        self.master.title("Dotter")
        self.pack(fill=BOTH, expand=0)

        if self.first_open:
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
        #canvas.create_rectangle(2, 2, 52, 52, outline="#111111", fill="#fb0")

        #get_box_shade(cur_val, maximum)

        #print(df.loc[cur_day][1]) #column 1 (column is 2nd index of loc)
        cur_day = 0
        cur_data = 0
        ppt_len = len(df)
        grid_width = 18
        grid_height = 7
        original_grid_height = grid_height
        for j in range(grid_width, 0, -1):
            xpo = j * square_dim #important
            
            if j == grid_width:
                grid_height = last_weekday + 1
            else:
                grid_height = original_grid_height
                
            for i in range(grid_height, 0, -1):
                ypo = i * square_dim #important

                #fill_color = "#fb0"
                fill_color = "#fff"
                
                if cur_day < ppt_len:  
                    cur_data = df.loc[ppt_len - 1 - cur_day][1]
                    #print(cur_data)
                    cur_day += 1
                    fill_color = self.get_box_shade(cur_data, maximum)
                
                
                self.canvas.create_rectangle(gsp_x1 + xpo, gsp_y1 + ypo, gsp_x2 + xpo, gsp_y2 + ypo, outline="#111111", fill=fill_color) #important
                
                #print(gsp_x2 + xpo, gsp_y2 + ypo) #2) final value: 382 162 
                #print(gsp_x1 + xpo, gsp_y1 + ypo) #1) final value: 362 142
        date_marker_color = "white"
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 30, anchor=CENTER, font="Purisa",text="M", fill=date_marker_color)
        #canvas.create_text(gsp_x1 + 10, gsp_y1 + 50, anchor=CENTER, font="Purisa",text="T", fill=date_marker_color)
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 70, anchor=CENTER, font="Purisa",text="W", fill=date_marker_color)
        #canvas.create_text(gsp_x1 + 10, gsp_y1 + 90, anchor=CENTER, font="Purisa",text="T", fill=date_marker_color)
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 110, anchor=CENTER, font="Purisa",text="F", fill=date_marker_color)
        #canvas.create_text(gsp_x1 + 10, gsp_y1 + 130, anchor=CENTER, font="Purisa",text="S", fill=date_marker_color)
        self.canvas.create_text(gsp_x1 + 10, gsp_y1 + 150, anchor=CENTER, font="Purisa",text="S", fill=date_marker_color)
        
        #weird white border between canvas and button is from top of canvas changing the order got rid of it idk

        #shows the current file
        self.canvas.create_text(canvas_width / 2, 15, anchor=CENTER, font="Purisa",text=self.current_file_name + ".xlsx", fill=date_marker_color)
        
        

        
        self.canvas.pack(fill=BOTH, expand=True) #important
        
root = tk.Tk()

ex = grid()
#ex.configure(bg='#FFDD00')
#ex.pack(tk.BOTH, expand=True)
#c = tk.Canvas(root, height=180, width=500, bg='white')
#c.pack(fill=tk.BOTH, expand=True)

#c.configure(bg='#FFDD00')
#c.bind('<Configure>', create_grid)

root.configure(bg = "black")
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




"""
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()
"""
