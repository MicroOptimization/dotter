"""
TO-DO
-----
Data:
-Incrementalization of spreadsheet
-spreadsheet updating
--getting current date

Frontend
-Showing
-Dot Darkening based on productivity progress
-Grid display

Very Frontend
-Make this a usable app somehow. (web app, android, idk)
"""
from datetime import date
import pandas
import tkinter as tk

date_today = date.today()
#We're gonna use this^ to check if there's an activity
#entry for today or not

#print("Today's date:", date_today)

sheet_name = "data"

df = pandas.read_excel(sheet_name + ".xlsx")

#print(df)
#print(df.index)


#print(df.loc[0]) #important for later
#print("Len: " , len(df)) #important for later [number of rows]
#print(df.loc[0][0]) #column 1 (column is 2nd index of loc)

"""
#iterates through my spreadsheet row by row
for i in range(len(df)):
    print(df.loc[i])
"""

root = tk.Tk()
# place a label on the root window

message = tk.Label(root, text=sheet_name)
message.pack()
root.geometry("500x200")




# keep the window displaying
root.mainloop()

